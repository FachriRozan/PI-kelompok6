import os
import glob
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
import re

# Inisialisasi Stopword Remover dan Stemmer untuk bahasa Indonesia
stopword_factory = StopWordRemoverFactory()
stemmer_factory = StemmerFactory()
stopword = stopword_factory.create_stop_word_remover()
stemmer = stemmer_factory.create_stemmer()

# Direktori dokumen
dir = 'Koprus_PI'

# Mendapatkan daftar file txt dalam direktori
files = glob.glob(os.path.join(dir, '*.txt'))

# Fungsi untuk melakukan preprocessing pada dokumen
def preprocess_document(document_text):
    # Hapus bagian "URL:" dan "Judul:"
    document_text = re.sub(r'URL:.*?Judul:*?', '', document_text, flags=re.DOTALL)
    
    clean_document = stopword.remove(document_text)

    # Stemming kata-kata
    stemmed_document = []
    for word in clean_document.split():
        stemmed_word = stemmer.stem(word)
        stemmed_document.append(stemmed_word)

    # Tokenisasi dokumen
    tokenized_document = nltk.word_tokenize(' '.join(stemmed_document))

    return tokenized_document

# Proses dokumen dan gabungkan hasil tokenizer dalam satu file
tokenized_documents = []
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

        # Tokenisasi, stemming, dan hapus stopwords pada teks di bawah "Judul:"
        tokenized_clean_document = preprocess_document(text)
        tokenized_documents.extend(tokenized_clean_document)
        print(
            f"Dokumen {len(tokenized_documents)} berhasil di-token, dibersihkan, dan dipreprocessed")

# Simpan hasil tokenisasi ke dalam satu file
with open('tokenized_documents.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(tokenized_documents))

# Fungsi untuk mengindeks semua kata yang sudah di-token di dalam dokumen dan menyimpan indeks ke dalam file
def index_tokenized_words_in_documents(tokenized_documents, output_file_path):
    word_index_dict = {}

    # Iterasi melalui dokumen yang sudah di-token
    for document_index, tokenized_document in enumerate(tokenized_documents):
        for word_index, word in enumerate(tokenized_document):
            if word not in word_index_dict:
                word_index_dict[word] = []
            word_index_dict[word].append((document_index + 1, word_index))
            word_index_list = word_index_dict[word]
            word_index_list.sort()

    # Simpan indeks kata ke dalam file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for word, document_index_and_word_index_list in word_index_dict.items():
            f.write(f'{word}: {document_index_and_word_index_list}\n')

# Indeks semua kata yang sudah di-token di dalam dokumen dan simpan indeks ke dalam satu file
index_tokenized_words_in_documents([tokenized_documents], 'index.txt')
