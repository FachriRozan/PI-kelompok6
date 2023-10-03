import os
import re
import nltk
import webbrowser
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from Sastrawi.Tokenization import Tokenizer

nltk.download('punkt')
nltk.download('stopwords')

# Fungsi untuk membaca dan memproses dokumen
def preprocess_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Hilangkan tanda baca
        content = re.sub(r'[^\w\s]', '', content)
        # Konversi ke huruf kecil
        content = content.lower()
        # Ekstrak stopwords dari konten dokumen
        tokenizer = Tokenizer()

        words = nltk.word_tokenize(content)
        stopwords_from_doc = [word for word in words if word in stopwords_ind]
        print(words)
        return content, stopwords_from_doc

# Mendapatkan daftar stopwords Bahasa Indonesia
stopwords_ind = set(stopwords.words('indonesian'))

# Mendefinisikan folder corpus
corpus_folder = 'Koprus_PI'  # Ganti dengan path folder corpus Anda

# Mengindeks dokumen dan menghitung TF-IDF
documents = []
document_urls = []
document_stopwords = []
for filename in os.listdir(corpus_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(corpus_folder, filename)
        content, doc_stopwords = preprocess_document(file_path)
        documents.append(content)
        document_stopwords.append(' '.join(doc_stopwords))  # Gabungkan stopwords menjadi string
        # Ekstrak judul dan URL dari dokumen
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('URL:'):
                    url = line.split(' ')[1].strip()
                    document_urls.append(url)
                    break

# Gabungkan stopwords dari dokumen dengan stopwords bahasa Indonesia
combined_stopwords = list(stopwords_ind) + document_stopwords

# Hitung TF-IDF
vectorizer = TfidfVectorizer(stop_words=combined_stopwords)  # Gunakan stopwords yang telah digabungkan
tfidf_matrix = vectorizer.fit_transform(documents)

# Membuat query
query = input('masukkan kata kunci pencarian: ')
query = query.lower()

# Transformasi query ke bentuk TF-IDF
query_vector = vectorizer.transform([query])

# Hitung skor kemiripan (cosine similarity) antara query dan dokumen
cosine_similarities = tfidf_matrix.dot(query_vector.T).toarray().flatten()

# Mengurutkan dokumen berdasarkan skor kemiripan
sorted_document_indices = cosine_similarities.argsort()[::-1][:1]

# Menampilkan hasil (judul, URL, dan stopwords dari dokumen)
j=0
for i in sorted_document_indices:
    j+=1
    print(j)
    print("Judul:", os.path.splitext(os.path.basename(os.listdir(corpus_folder)[i]))[0])
    print("Skor Kemiripan:", cosine_similarities[i])
    print("="*50)
    
while True:
    try:
        # Meminta input berupa angka dari pengguna
        angka = int(input("Pilih nomor website yang diinginkan (1-5): "))
        
        # Memeriksa apakah input berada dalam rentang 1-5
        if 1 <= angka <= 5:
            # Mendapatkan indeks dokumen yang sesuai dengan pilihan pengguna
            selected_index = sorted_document_indices[angka - 1]
            
            # Membuka URL terkait dengan dokumen yang dipilih
            webbrowser.open(document_urls[selected_index])
            break  # Keluar dari loop setelah membuka URL
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 5.")
    except ValueError:
        print("Masukkan angka yang valid.")