from transformers import pipeline
translator = pipeline("translation_en_to_fr")
text = "Natural language processing is very interesting."
result = translator(text)
print("French Translation:")
print(result[0]['translation_text'])
