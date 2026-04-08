import nltk
from nltk.tag import DefaultTagger, UnigramTagger
train_data = [
    [("The", "DT"), ("dog", "NN"), ("barks", "VB")],
    [("A", "DT"), ("cat", "NN"), ("runs", "VB")]
]
default_tagger = DefaultTagger("NN")
unigram_tagger = UnigramTagger(train_data, backoff=default_tagger)
sentence = ["The", "cat", "runs"]
print("Tagged Sentence:")
print(unigram_tagger.tag(sentence))
