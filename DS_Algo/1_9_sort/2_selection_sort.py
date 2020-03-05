def selection_sort(inp):
    answer = []
    for i in range(len(inp)-1):
        min_j = i
        for j in range(i+1, len(inp)):
            if inp[min_j] > inp[j]:
                min_j = j
        inp[i], inp[min_j] = inp[min_j], inp[i]
    answer = inp
    return answer


def test_selection_sort():
    inp = [1,5,4,3,2]
    ans = [1,2,3,4,5]
    assert(selection_sort(inp) == ans)
    print('테스트 통과!')


if __name__ == '__main__':
    test_selection_sort()