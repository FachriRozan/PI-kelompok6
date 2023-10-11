import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the TF-IDF matrix from a .npy file
tfidf_matrix = np.load('tfidf_matrix.npy')

# Load document information from a JSON file
with open('data.json', 'r', encoding='utf-8') as json_file:
    document_data = json.load(json_file)
document_names = [entry["title"] for entry in document_data]

# Input query
query = input("Enter your query: ")

# Create a TF-IDF vectorizer and fit it on the entire corpus (query and documents)
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([query] + document_names)

# Calculate the cosine similarity between the query and all documents
cosine_similarities = linear_kernel(tfidf_matrix[0:1], tfidf_matrix[1:])

# Sort the results by similarity
similarity_scores = list(enumerate(cosine_similarities.flatten()))
similarity_scores.sort(key=lambda x: x[1], reverse=True)

# Display search results
print("\nSearch Results:")
for rank, (doc_index, score) in enumerate(similarity_scores, start=1):
    document = document_data[doc_index]
    document_name = document["title"]
    document_url = document["url"]

    print(f"Rank: {rank}")
    print(f"Document Name: {document_name}")
    print(f"Similarity Score: {score:.7f}")
    print(f"Document URL: {document_url}")
    print()
