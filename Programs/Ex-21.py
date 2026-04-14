import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import RegexpParser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = "The intelligent student solved the difficult problem"
words = word_tokenize(sentence)
tags = pos_tag(words)
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(tags)
print("Noun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree)
        print(phrase)
