import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=True)

# Open the file for reading
with open('tokenized_documents.txt', 'r', encoding='utf-8') as f:
    # Read the contents of the file
    documents = [line.strip() for line in f]

# Close the file
f.close()

# Calculate the TF-IDF vectors for the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert the TF-IDF matrix to a dense NumPy array
tfidf_matrix_dense = tfidf_matrix.toarray()

# Save the dense TF-IDF matrix to a NumPy binary file
np.save('tfidf_matrix.npy', tfidf_matrix_dense)