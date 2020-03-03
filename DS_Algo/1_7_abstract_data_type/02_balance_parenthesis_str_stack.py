def balance_parenthesis_str_stack(s):
    stk = []
    balanced = True
    index = 0

    while index < len(s) and balanced:
        symbol = s[index]

        if symbol == '(':
            stk.append(symbol)
        # symol == ')'
        else:
            # 비어있으면
            if len(stk) == 0:
                balanced = False
            # 비어있지 않으면
            else:
                stk.pop()
        index += 1

    if balanced and len(stk) == 0:
        return True
    else:
        return False
    # for i, ch in enumerate(s):
    #     if ch == '(':
    #         stk.append(ch)
    #         if s[i+1] == ch:
    #             stk.append(ch)
    #         else:
    #             stk.pop()
    #             stk.pop()
    # if len(stk) == 0 and balanced == True:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    print(balance_parenthesis_str_stack('((())'))
    print(balance_parenthesis_str_stack('(()'))