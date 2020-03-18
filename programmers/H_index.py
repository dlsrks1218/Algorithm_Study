def solution(inp1):
    ans = 0
    cit = sorted(inp1, reverse=True)
    h = 0
    
    for i, c in enumerate(cit):
        h = len(cit) - i
        bigger = [b for b in cit if b >= h]

        if len(bigger) >= h:
            ans = h
            break

    return ans


def test(inp1, ans):
    try:
        assert len(inp1) >= 1 and len(inp1) <= 10000
        assert max(inp1) <= 10000 and min(inp1) >= 0
        assert(solution(inp1) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test([3,0,6,1,5], 3)
    test([4,1,4,2,5,3,6],4)
    test([1,7,0,1,6,5], 3)