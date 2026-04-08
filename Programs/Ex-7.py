import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
text = "Natural language processing is interesting"
words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)
print("POS Tags:")
print(pos_tags)
