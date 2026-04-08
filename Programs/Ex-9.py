import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger
nltk.download('punkt')
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+$', 'CD'),
    (r'.*', 'NN')
]
tagger = RegexpTagger(patterns)
sentence = "The dog is running in the gardens"
words = word_tokenize(sentence)
print(tagger.tag(words))
