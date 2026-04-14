import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
text = "John went to the store. He bought milk."
sentences = sent_tokenize(text)
entities = []
resolved_text = []
for sentence in sentences:
    words = word_tokenize(sentence)
    for i, word in enumerate(words):
        if word in ["He", "She", "They"] and entities:
            words[i] = entities[-1]
    for word in words:
        if word.istitle():
            entities.append(word)
    resolved_text.append(" ".join(words))
print("Resolved Text:")
print(" ".join(resolved_text))
