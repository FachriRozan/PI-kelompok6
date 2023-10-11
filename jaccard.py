import json
import time

# Define a function to compute the Jaccard similarity between two sets
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union

# Load tokenized documents from file
with open('tokenized_documents.txt', 'r', encoding='utf-8') as f:
    tokenized_documents = [set(line.strip().split()) for line in f.readlines()]

# Load document names from the JSON file
with open('data.json', 'r', encoding='utf-8') as f:
    document_data = json.load(f)
    document_names = [entry["title"] for entry in document_data]

# Input query
query = input("Masukkan query: ")

# Tokenize the query
query_tokens = set(query.split())

start_time = time.time()

# Calculate Jaccard similarities with the query for each document
similarities = []
for i, doc_tokens in enumerate(tokenized_documents):
    similarity = jaccard_similarity(query_tokens, doc_tokens)
    similarities.append((i, similarity))

# Sort the results by similarity
similarities.sort(key=lambda x: x[1], reverse=True)

# Display search results
print("\nHasil Pencarian:")
for rank, (doc_index, score) in enumerate(similarities, start=1):
    document_name = document_names[doc_index]
    document_url = document_data[doc_index].get("url", "URL not found")
    print(f"Rank: {rank}")
    print(f"Nama Dokumen: {document_name}")
    print(f"Skor: {score:.7f}")
    print(f"Document URL: '{document_url}'\n")

end_time = time.time()

print(f"Waktu eksekusi: {end_time - start_time:.9f} detik")
