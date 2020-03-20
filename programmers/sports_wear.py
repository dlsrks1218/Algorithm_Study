def solution(n, lost, reserve):
    clothes_lst = [1]*n
    # print(clothes_lst)
    for r in reserve:
        clothes_lst[r-1] += 1
    # print(clothes_lst)
    for l in lost:
        clothes_lst[l-1] -= 1
    # print(clothes_lst)

    for i, v in enumerate(clothes_lst):
        if i > 0 and v == 0 and clothes_lst[i-1] > 1:
            clothes_lst[i-1] = 1
            clothes_lst[i] = 1
        elif i < n-1 and v == 0 and clothes_lst[i+1] > 1:
            clothes_lst[i] = 1
            clothes_lst[i+1] = 1
    # print(clothes_lst)
    return n-clothes_lst.count(0)


def test(inp1, inp2, inp3, ans):
    try:
        assert inp1 >= 2 and inp1 <= 30
        assert len(inp2) >= 1 and len(inp2) <= inp1
        assert len(inp3) >= 1 and len(inp3) <= inp1
        assert(solution(inp1, inp2, inp3) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test(5, [2,4], [1,3,5], 5)
    test(5, [2,4], [3], 4)
    test(3, [3], [1], 2)
    test(10, [3,9,10],[3,8,9], 9)