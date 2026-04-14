import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [1.0]
Det -> 'the' [0.5] | 'a' [0.5]
N -> 'cat' [0.5] | 'dog' [0.5]
V -> 'chased' [0.6] | 'saw' [0.4]
""")
sentence = "the cat chased a dog".split()
parser = ViterbiParser(grammar)
for tree in parser.parse(sentence):
    print(tree)
