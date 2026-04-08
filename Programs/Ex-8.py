import random
training_data = {
    "dog": ["NN"],
    "barks": ["VB"],
    "cat": ["NN"],
    "runs": ["VB"],
    "happy": ["JJ"]
}
sentence = "dog runs happy"
words = sentence.split()
print("Stochastic POS Tags:")
for word in words:
    if word in training_data:
        tag = random.choice(training_data[word])
    else:
        tag = "NN"
    print(word, "->", tag)
