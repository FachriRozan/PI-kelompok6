import os

# Mendefinisikan fungsi pencarian teks dalam berkas
def cari_dalam_berkas(lokasi_folder, query):
    berkas_relevan = []
    for nama_berkas in os.listdir(lokasi_folder):
        path_berkas = os.path.join(lokasi_folder, nama_berkas)
        if os.path.isfile(path_berkas) and nama_berkas.endswith('.txt'):
            with open(path_berkas, 'r', encoding='utf-8') as berkas:
                teks = berkas.read()
                if query.lower() in teks.lower():
                    berkas_relevan.append(path_berkas)
    return berkas_relevan

# Lokasi folder berkas teks
lokasi_folder = 'Koprus_PI'

# Input query dari pengguna
query = input("Masukkan query: ")

# Melakukan pencarian dalam folder
berkas_relevan = cari_dalam_berkas(lokasi_folder, query)

# Menampilkan hasil pencarian
n=0
if berkas_relevan:
    print("Berkas relevan ditemukan:")
    for berkas in berkas_relevan:
        print(berkas)
        n+=1
else:
    print("Tidak ada berkas yang relevan ditemukan.")

print(n)