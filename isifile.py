import os
import re
import string
import glob

# Daftar ekstensi file yang ingin Anda proses
ekstensi_file = '.txt'

# Direktori folder yang berisi file-file teks
folder_path = 'Koprus_PI'

# Mendapatkan daftar file dengan ekstensi .txt dalam folder
file_list = glob.glob(os.path.join(folder_path, '*' + ekstensi_file))

# Iterasi melalui setiap file dan melakukan operasi yang diinginkan
for file_path in file_list:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Menyimpan URL dan Judul
    url_match = re.search(r'URL:(.*?)\n', content)
    judul_match = re.search(r'Judul:(.*?)\n', content)

    if url_match:
        url = url_match.group(1).strip()
    else:
        url = ''

    if judul_match:
        # Menghilangkan "- Wikipedia bahasa Indonesia, ensiklopedia bebas" dari judul
        judul = re.sub(r'- Wikipedia bahasa Indonesia, ensiklopedia bebas', '', judul_match.group(1).strip())
    else:
        judul = ''

    # Lakukan operasi penghapusan dan normalisasi teks di sini
    content = re.sub(r'URL:.*?Judul:.*?\n', '', content, flags=re.DOTALL)
    content = re.sub(r'\[sunting \| sunting sumber\]', '', content)
    content = re.sub(r'\[\d+\]', '', content)
    content = re.sub(r'\–', ' ', content)
    content = re.sub(r'\n', ' ', content)
    content = content.translate(str.maketrans('', '', string.punctuation))
    content_lowercase = content.lower()

    # Menyimpan URL, Judul, dan hasilnya kembali ke file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('URL: ' + url + '\n')
        file.write('Judul: ' + judul + '\n')
        file.write(content_lowercase)

print('Operasi selesai pada semua file teks dalam folder.')
