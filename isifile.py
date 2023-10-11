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

    # Lakukan operasi penghapusan dan normalisasi teks di sini
    content = re.sub(r'URL:.*?Judul:.*?\n', '', content, flags=re.DOTALL)
    content = re.sub(r'\[sunting \| sunting sumber\]', '', content)
    content = re.sub(r'\[\d+\]', '', content)
    content = re.sub(r'\–', ' ', content)
    content = re.sub(r'\n', ' ', content)
    content = re.sub(r'Pemisah Isi File', '', content)
    content = content.translate(str.maketrans('', '', string.punctuation))
    content_lowercase = content.lower()

    # Menyimpan hasilnya kembali ke file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content_lowercase)

print('Operasi selesai pada semua file teks dalam folder.')
