grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}
sentence = ["the", "cat", "chased", "a", "dog"]
chart = [[] for _ in range(len(sentence)+1)]
chart[0].append(("S", ["NP", "VP"], 0))
for i in range(len(chart)):
    for state in chart[i]:
        lhs, rhs, dot = state
        if dot < len(rhs):
            next_symbol = rhs[dot]
            if next_symbol in grammar:
                for rule in grammar[next_symbol]:
                    chart[i].append((next_symbol, rule, 0))
            elif i < len(sentence) and sentence[i] == next_symbol:
                chart[i+1].append((lhs, rhs, dot+1))
        else:
            for prev in chart[i]:
                plhs, prhs, pdot = prev
                if pdot < len(prhs) and prhs[pdot] == lhs:
                    chart[i].append((plhs, prhs, pdot+1))
print("Earley Chart:")
for i, states in enumerate(chart):
    print(i, states)
