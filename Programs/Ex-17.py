import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
word = "bank"
synsets = wordnet.synsets(word)
print("Synsets of", word)
for syn in synsets:
    print("Name:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print()
