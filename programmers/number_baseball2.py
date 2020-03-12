import itertools

def func(x, y):
    x = list(x)
    y = list(y)
    s, b = 0, 0

    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i:
                s+=1
            else:
                b+=1
    return [s, b]


def solution(inp_lst):
    ans = 0
    
    num = list(map(lambda x: str(x[0]), inp_lst))
    cnt = list(map(lambda x : [x[1], x[2]], inp_lst))

    all_case = list(itertools.permutations(range(1, 10), 3))
    all_case = list(map(lambda x: list(map(str, x)), all_case))
    
    for case in all_case:
        if [func(case, y) for y in num] == cnt: 
            ans+=1

    return ans


def test(inp_lst, ans):
    try:
        assert len(inp_lst) >= 1 and len(inp_lst) <=100
        assert(solution(inp_lst) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]], 2)