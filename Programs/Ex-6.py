import random
from collections import defaultdict
text = "I love natural language processing and I love machine learning"
words = text.split()
bigrams = defaultdict(list)
for i in range(len(words)-1):
    bigrams[words[i]].append(words[i+1])
word = random.choice(words)
result = [word]
for i in range(10):
    next_words = bigrams.get(word)
    if not next_words:
        break
    word = random.choice(next_words)
    result.append(word)
print("Generated Text:")
print(" ".join(result))
