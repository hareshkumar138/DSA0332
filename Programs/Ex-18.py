import re
def parse_expression(expr):
    pattern = r'(\w+)\((.*)\)'
    match = re.match(pattern, expr)
    if match:
        predicate = match.group(1)
        arguments = match.group(2).split(',')
        print("Predicate:", predicate)
        print("Arguments:", arguments)        
    else:
        print("Invalid Expression")
expression = "Loves(John,Mary)"
parse_expression(expression)
