def ends_with_ab(string):
    state = 0
    for char in string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0
    if state == 2:
        return True
    return False
word = input("Enter a string: ")
if ends_with_ab(word):
    print("String accepted (ends with 'ab')")
else:
    print("String rejected")
