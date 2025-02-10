import os
import json
import base64
import gspread

from google.oauth2.service_account import Credentials
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from zoneinfo import ZoneInfo


# Fungsi untuk mendapatkan credentials dari environment variable
def get_google_credentials():
    service_account_key_base64 = os.getenv("GOOGLE_SERVICE_ACCOUNT_KEY")
    if service_account_key_base64:
        service_account_json = base64.b64decode(service_account_key_base64).decode("utf-8")
        service_account_info = json.loads(service_account_json)
        return Credentials.from_service_account_info(service_account_info, scopes=[
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ])
    return None

def index(request):
    credentials = get_google_credentials()
    if not credentials:
        return JsonResponse({'message': 'Google credentials tidak ditemukan.', 'status': 'error'})

    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_key('1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI')
    worksheet_meja = spreadsheet.get_worksheet(0)
    data_meja = worksheet_meja.get_all_records()
    penghuni_data = {row['Nama_meja']: row['Penghuni'] for row in data_meja}
    
    return render(request, 'index.html', {'penghuni_data': penghuni_data})

def reserveDesk(request):
    # Ambil waktu sekarang dalam timezone Asia/Jakarta
    now = timezone.now().astimezone(ZoneInfo("Asia/Jakarta"))
    
    # Batasi reservasi hanya antara 07:00 hingga 13:00
    if not (7 <= now.hour < 13):
        return JsonResponse({'message': 'Reservasi hanya dapat dilakukan antara pukul 07:00 hingga 13:00.', 'status': 'error'})

    credentials = get_google_credentials()
    if not credentials:
        return JsonResponse({'message': 'Google credentials tidak ditemukan.', 'status': 'error'})

    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_key('1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI')
    worksheet_meja = spreadsheet.get_worksheet(0)
    data_meja = worksheet_meja.get_all_records()
    penghuni_data = {row['Nama_meja']: row['Penghuni'] for row in data_meja}
    
    worksheet_token = spreadsheet.get_worksheet(1)
    data_token = worksheet_token.get_all_records()
    token_dict = {row['token'].lower(): row['Nama'] for row in data_token}
    
    token = request.POST.get('token', '').strip().lower()
    desk = request.POST.get('desk', '').strip().lower()
    
    if not token or not desk:
        return JsonResponse({'message': 'Token atau desk tidak boleh kosong', 'status': 'error', 'penghuni_data': penghuni_data})
    
    if token in token_dict:
        namapenghuni = token_dict[token]
        if namapenghuni in penghuni_data.values():
            return JsonResponse({'message': f'Reservasi ditolak. {namapenghuni} sudah memiliki meja.', 'status': 'error', 'penghuni_data': penghuni_data})
        
        try:
            cell = worksheet_meja.find(desk)
            row = cell.row
            worksheet_meja.update_cell(row, 2, namapenghuni)
            data_meja = worksheet_meja.get_all_records()
            penghuni_data = {row['Nama_meja']: row['Penghuni'] for row in data_meja}
            return JsonResponse({'message': 'Token valid, penghuni berhasil diperbarui', 'status': 'success', 'penghuni_data': penghuni_data})
        except gspread.exceptions.CellNotFound:
            return JsonResponse({'message': 'Nama meja tidak ditemukan', 'status': 'error', 'penghuni_data': penghuni_data})
    else:
        return JsonResponse({'message': 'Token tidak ditemukan', 'status': 'error', 'penghuni_data': penghuni_data})
