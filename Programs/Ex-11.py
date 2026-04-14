grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": ["the", "a"],
    "N": ["cat", "dog"],
    "V": ["chased", "saw"]
}
sentence = ["the", "cat", "chased", "a", "dog"]
def parse_S(words):
    if parse_NP(words[:2]) and parse_VP(words[2:]):
        return True
    return False
def parse_NP(words):
    if len(words) == 2 and words[0] in grammar["Det"] and words[1] in grammar["N"]:
        return True
    return False
def parse_VP(words):
    if len(words) == 3 and words[0] in grammar["V"] and parse_NP(words[1:]):
        return True
    return False
result = parse_S(sentence)
print("Sentence:", " ".join(sentence))
print("Parsing Result:", result)
