import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
text = "The cats are running faster than the dogs"
words = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
print("Original Words:", words)
print("\nLemmatized Words:")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
