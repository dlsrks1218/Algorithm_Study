def solution(s):
    ans = []

    s = s[1:-1]
    # print(s)

    tup = []
    stack = ''

    s = s.replace('},', '}')
    for idx, ch in enumerate(s):
        stack += ch
        if ch == '}':
            tup.append(stack)
            stack = ''
            if idx+1 < len(s) and s[idx+1] == ',':
                stack = stack[:-1]

    # 길이 순 정렬
    tup = sorted(tup, key=len)
        
    for idx, item in enumerate(tup):
        item = item.replace('{', '')
        item = item.replace('}', '')
        tup[idx] = item

    # for item in tup:
    #     print(item)

    for i in range(len(tup)):
        tup[i] = tup[i].split(',')
        # print(tup[i], type(tup[i]))
        if i == 0:
            ans.append(int(''.join(tup[i])))
        if i < len(tup) - 1:
            ans.append(int(''.join(list(set(tup[i+1].split(',')) - set(tup[i])))))
    
    # print(ans)

    return ans


def test(s, ans):
    try:
        assert len(s) >= 5 and len(s) <= 1000000
        # assert min(s) >= 1 and max(s) <= 100000
        # assert min(len(solution(s))) >= 1 and max(len(solution(s))) <= 500
        assert(solution(s) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test("{{2},{2,1},{2,1,3},{2,1,3,4}}", [2, 1, 3, 4])
    test("{{1,2,3},{2,1},{1,2,4,3},{2}}", [2, 1, 3, 4])
    test("{{20,111},{111}}", [111, 20])