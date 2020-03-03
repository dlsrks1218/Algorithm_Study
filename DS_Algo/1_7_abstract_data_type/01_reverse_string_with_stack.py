def reverse_string_with_stack(s):
    stk = []
    revStr = ''

    for c in s:
        stk.append(c)
    
    while stk:
        revStr += stk.pop()
    
    return revStr


if __name__ == '__main__':
    s1 = '버피는 천사다.'
    print(s1)
    print(reverse_string_with_stack(s1))