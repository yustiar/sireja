import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime




def index(request):
    

    dfmeja = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/' +
        '1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI' +
        '/export?gid=0' +
        '&format=csv',
        dtype=str)

    dfmeja = dfmeja.fillna('')
    penghuni_data = dfmeja.set_index('Nama_meja')['Penghuni'].to_dict()


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
    dfmeja = pd.DataFrame(worksheet_meja.get_all_records())
    dfmeja = dfmeja.fillna('')
    penghuni_data = dfmeja.set_index('Nama_meja')['Penghuni'].to_dict()

    # Baca data token dari Google Sheets
    worksheet_token = spreadsheet.get_worksheet(1)  # Assuming the second sheet (index 1)
    dftoken = pd.DataFrame(worksheet_token.get_all_records())
    dftoken['token'] = dftoken['token'].str.lower()

    # Ambil data dari POST request
    token = request.POST.get('token', '').strip().lower()
    desk = request.POST.get('desk', '').strip().lower()

    # Validasi token dan desk
    if not token or not desk:
        response = {
            'message': 'Token atau desk tidak boleh kosong',
            'status': 'error',
            'penghuni_data': penghuni_data
        }
    elif token in dftoken['token'].values:
        # Ambil nama penghuni dari token
        namapenghuni = dftoken.loc[dftoken['token'] == token, 'Nama'].values[0]

        # Periksa apakah nama penghuni sudah ada di kolom "Penghuni"
        if namapenghuni in dfmeja['Penghuni'].values:
            response = {
                'message': f'Reservasi ditolak. {namapenghuni} sudah memiliki meja.',
                'status': 'error',
                'penghuni_data': penghuni_data
            }
        else:
            # Lanjutkan jika nama belum ada di kolom "Penghuni"
            try:
                cell = worksheet_meja.find(desk)
                row = cell.row
                worksheet_meja.update_cell(row, 2, namapenghuni)  # Column B is the 2nd column

                # Perbarui penghuni_data setelah perubahan
                dfmeja = pd.DataFrame(worksheet_meja.get_all_records())
                dfmeja = dfmeja.fillna('')
                penghuni_data = dfmeja.set_index('Nama_meja')['Penghuni'].to_dict()

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

    return JsonResponse(response)
