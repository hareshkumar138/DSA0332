from nltk.stem import PorterStemmer
words = ["running", "playing", "studies", "happiness", "flying"]
stemmer = PorterStemmer()
print("Word Stemming using Porter Stemmer:\n")
for word in words:
    print(word, "->", stemmer.stem(word))
