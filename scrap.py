import requests
from bs4 import BeautifulSoup
import os

# Daftar URL halaman web
daftar_url = [
    '','','',''
]

# Class yang ingin Anda cari di elemen <div>
class_target = 'mw-parser-output'

# Class yang ingin Anda hindari
class_yang_dihindari = ['reflist', 'refbegin', 'sidebar', 'navbox', 'box-Expand_language', 'infobox']

# Direktori tempat Anda ingin menyimpan file
output_directory = 'Koprus_PI'

# Membuat direktori jika belum ada
os.makedirs(output_directory, exist_ok=True)

for url in daftar_url:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mengambil URL halaman web
        page_url = response.url

        # Mengambil judul dari halaman (misalnya, dari elemen <title>)
        page_title = soup.title.string

        # Menghapus elemen dengan class yang dihindari
        for class_name in class_yang_dihindari:
            for elemen in soup.find_all(class_=class_name):
                elemen.extract()

        # Mengambil semua elemen <div> dengan class tertentu
        div_elements = soup.find_all('div', class_=class_target)

        # Menggabungkan URL, judul, dan konten div ke dalam format teks
        output_text = f"URL: {page_url}\nJudul: {page_title}\n\n"

        for div in div_elements:
            output_text += div.get_text() + '\n\n'

        # Menyimpan data dalam file .txt (menggunakan URL sebagai nama file)
        file_name = os.path.join(output_directory, url.split('/')[-1].split('?')[0] + '.txt')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(output_text)

        print(f"Data dari {page_url} telah disimpan dalam '{file_name}'.")
    else:
        print(f"Gagal mengambil {url}.")
