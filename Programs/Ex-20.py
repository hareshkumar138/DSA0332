from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "Natural language processing is interesting",
    "Machine learning is a part of artificial intelligence",
    "Deep learning is used in NLP"
]
query = ["natural language"]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + query)
scores = (tfidf_matrix[-1] * tfidf_matrix[:-1].T).toarray()
print("Document Similarity Scores:")
print(scores)
