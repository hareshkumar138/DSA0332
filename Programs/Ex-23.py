from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text = [
    "Natural language processing is a field of AI",
    "It helps computers understand human language",
    "NLP is used in chatbots and translation systems"
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(text)
similarity = cosine_similarity(tfidf_matrix)
print("Coherence Matrix:")
print(similarity)
