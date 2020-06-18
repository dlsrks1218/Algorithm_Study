def stringTokenizer(string):
    result = []
    for ch in string:
        result.append(ch)
    oper = ['+', '-', '*', '/']
    brac = ['(', ')']

    operator = []
    number = []
    for ch in string:
        if ch in oper:
            operator.append(ch)
        elif ch in 

    return result

string = '1+2*(3-4)'
print(stringTokenizer(string))