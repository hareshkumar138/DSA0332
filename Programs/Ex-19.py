import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
sentence = "He went to the bank to deposit money"
word = "bank"
sense = lesk(word_tokenize(sentence), word)
print("Word Sense:", sense)
print("Definition:", sense.definition())
