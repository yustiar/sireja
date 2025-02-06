import requests
import pandas as pd
import pygsheets
import pytz

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
    # Tentukan zona waktu WIB
    wib = pytz.timezone("Asia/Jakarta")
    now = datetime.now(wib)
    print(now)

    # Baca data meja dari Google Sheets
    dfmeja = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/' +
        '1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI' +
        '/export?gid=0' +
        '&format=csv',
        dtype=str
    )
    dfmeja = dfmeja.fillna('')
    penghuni_data = dfmeja.set_index('Nama_meja')['Penghuni'].to_dict()

    # Periksa apakah waktu saat ini sudah setelah pukul 07:00 WIB
    if now.hour < 7:
        return JsonResponse({
            'message': 'Reservasi hanya dapat dilakukan setelah pukul 07:00 WIB',
            'status': 'error',
            'penghuni_data': penghuni_data
        })

    response = {}  # Variabel tunggal untuk menyimpan hasil eksekusi

    
    # Baca data token dari Google Sheets
    dftoken = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/' +
        '1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI' +
        '/export?gid=773815127' +
        '&format=csv',
        dtype=str
    )
    dftoken['token'] = dftoken['token'].str.lower()

    # Ambil data dari POST request
    token = request.POST.get('token', '').strip().lower()
    desk = request.POST.get('desk', '').strip().lower()

    # Baca data meja dari Google Sheets
    dfmeja = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/' +
        '1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI' +
        '/export?gid=0' +
        '&format=csv',
        dtype=str
    )
    dfmeja = dfmeja.fillna('')
    penghuni_data = dfmeja.set_index('Nama_meja')['Penghuni'].to_dict()

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
            gc = pygsheets.authorize(service_file=settings.GOOGLE_SHEET_CREDENTIALS_PATH)
            spreadsheet = gc.open_by_key('1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI')
            worksheet = spreadsheet.sheet1

            cell = worksheet.find(desk)
            if cell:
                row = cell[0].row
                worksheet.update_value(f'B{row}', namapenghuni)

                # Perbarui penghuni_data setelah perubahan
                dfmeja = pd.read_csv(
                    'https://docs.google.com/spreadsheets/d/' +
                    '1nAnBte1BKkBwr0wncALd7I8OBcQ6sqlYVnPu5kZpLVI' +
                    '/export?gid=0' +
                    '&format=csv',
                    dtype=str
                )
                dfmeja = dfmeja.fillna('')
                penghuni_data = dfmeja.set_index('Nama_meja')['Penghuni'].to_dict()

                response = {
                    'message': 'Token valid, penghuni berhasil diperbarui',
                    'status': 'success',
                    'penghuni_data': penghuni_data
                }
            else:
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