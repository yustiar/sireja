import gspread
import pytz
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

def index(request):
    # Define the scope and credentials for Google Sheets access
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.GOOGLE_SHEET_CREDENTIALS_PATH, scope)
    gc = gspread.authorize(credentials)

    # Open the spreadsheet by key
    spreadsheet = gc.open_by_key('1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI')

    # Baca data meja dari Google Sheets
    worksheet_meja = spreadsheet.get_worksheet(0)  # Assuming the first sheet (index 0)
    data_meja = worksheet_meja.get_all_records()

    # Mengolah data meja menjadi dictionary
    penghuni_data = {row['Nama_meja']: row['Penghuni'] for row in data_meja}

    return render(request, 'index.html', {'penghuni_data': penghuni_data})


def reserveDesk(request):
    # Define the scope and credentials for Google Sheets access
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.GOOGLE_SHEET_CREDENTIALS_PATH, scope)
    gc = gspread.authorize(credentials)

    # Open the spreadsheet by key
    spreadsheet = gc.open_by_key('1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI')

    # Baca data meja dari Google Sheets
    worksheet_meja = spreadsheet.get_worksheet(0)  # Assuming the first sheet (index 0)
    data_meja = worksheet_meja.get_all_records()

    # Mengolah data meja menjadi dictionary
    penghuni_data = {row['Nama_meja']: row['Penghuni'] for row in data_meja}

    # Baca data token dari Google Sheets
    worksheet_token = spreadsheet.get_worksheet(1)  # Assuming the second sheet (index 1)
    data_token = worksheet_token.get_all_records()
    token_dict = {row['token'].lower(): row['Nama'] for row in data_token}

    # Ambil data dari POST request
    token = request.POST.get('token', '').strip().lower()
    desk = request.POST.get('desk', '').strip().lower()

    response = {}  # Variabel tunggal untuk menyimpan hasil eksekusi

    wib = pytz.timezone("Asia/Jakarta")
    now = datetime.now(wib)
    
    # Periksa apakah waktu saat ini berada di antara 07:00 - 13:00 WIB
    if (7 <= now.hour < 16):
        # Validasi token dan desk
        if not token or not desk:
            response = {
                'message': 'Token atau desk tidak boleh kosong',
                'status': 'error',
                'penghuni_data': penghuni_data
            }
        elif token in token_dict:
            # Ambil nama penghuni dari token
            namapenghuni = token_dict[token]

            # Periksa apakah nama penghuni sudah ada di kolom "Penghuni"
            if namapenghuni in penghuni_data.values():
                response = {
                    'message': f'Reservasi ditolak. {namapenghuni} sudah memiliki meja.',
                    'status': 'error',
                    'penghuni_data': penghuni_data
                }
            else:
                # Lanjutkan jika nama belum ada di kolom "Penghuni"
                try:
                    # Temukan cell meja dan perbarui penghuni
                    cell = worksheet_meja.find(desk)
                    row = cell.row
                    worksheet_meja.update_cell(row, 2, namapenghuni)  # Column B is the 2nd column

                    # Perbarui penghuni_data setelah perubahan
                    data_meja = worksheet_meja.get_all_records()
                    penghuni_data = {row['Nama_meja']: row['Penghuni'] for row in data_meja}

                    response = {
                        'message': 'Token valid, penghuni berhasil diperbarui',
                        'status': 'success',
                        'penghuni_data': penghuni_data
                    }
                except gspread.exceptions.CellNotFound:
                    response = {
                        'message': 'Nama meja tidak ditemukan',
                        'status': 'error',
                        'penghuni_data': penghuni_data
                    }
        else:
            response = {
                'message': 'Token tidak ditemukan',
                'status': 'error',
                'penghuni_data': penghuni_data
            }
    else: 
        response = {
            'message': 'Reservasi hanya dapat dilakukan antara pukul 07:00 - 16:00 WIB',
            'status': 'error',
            'penghuni_data': penghuni_data
        }

    return JsonResponse(response)
