def pluralize(noun):
    if noun.endswith('y'):
        return noun[:-1] + 'ies'
    elif noun.endswith(('s','x','z','ch','sh')):
        return noun + 'es'
    else:
        return noun + 's'
word = input("Enter a noun: ")
plural = pluralize(word)
print("Plural form:", plural)
