grammar = {
    "singular_subject": ["he", "she", "it"],
    "plural_subject": ["they", "we"],
    "singular_verb": ["runs", "eats"],
    "plural_verb": ["run", "eat"]
}
sentence = input("Enter sentence: ").lower().split()
subject = sentence[0]
verb = sentence[1]
if subject in grammar["singular_subject"] and verb in grammar["singular_verb"]:
    print("Correct Agreement")
elif subject in grammar["plural_subject"] and verb in grammar["plural_verb"]:
    print("Correct Agreement")
else:
    print("Agreement Error")
