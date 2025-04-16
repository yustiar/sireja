import gspread
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
    worksheet_meja = spreadsheet.get_worksheet(0)
    data_meja = worksheet_meja.get_all_records()
    penghuni_data = {row['Nama_meja']: row['Penghuni'] for row in data_meja}
    
    worksheet_token = spreadsheet.get_worksheet(1)
    data_token = worksheet_token.get_all_records()
    token_dict = {row['token'].lower(): row['Nama'] for row in data_token}
    
    token = request.POST.get('token', '').strip().lower()
    desk = request.POST.get('desk', '').strip().lower()
    distance = request.POST.get('distance', '').strip()

    if distance:  # Pastikan 'distance' ada dan tidak kosong
        try:
            distance = float(distance)  # Ubah 'distance' ke tipe integer
        except ValueError:
            return JsonResponse({'message': 'Jarak tidak valid', 'status': 'error', 'penghuni_data': penghuni_data})

        # Cek jika jarak lebih dari 75 km
        if distance > 75:
            return JsonResponse({
                'message': 'Anda berada diluar jangkauan kantor',
                'status': 'error',
                'penghuni_data': penghuni_data  # Pastikan penghuni_data didefinisikan sebelumnya
            })

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
