import keyword

# ['False', 'None', 'True', '__peg_parser__',
# 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else',
# 'except', 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
# 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(keyword.kwlist)


def calculate1(a, b):
    c = a + b
    pass
    return c


print(calculate1(3, 9))
