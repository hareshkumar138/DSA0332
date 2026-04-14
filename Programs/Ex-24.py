def classify_dialog(sentence):
    if sentence.endswith("?"):
        return "Question"
    elif sentence.lower().startswith(("please", "do", "can you")):
        return "Request"
    else:
        return "Statement"
dialog = [
    "What is your name?",
    "Please open the door",
    "I am learning NLP"
]
for sentence in dialog:
    print(sentence, "->", classify_dialog(sentence))
