import quick_sort as q

def find_k_largest(inp, k):
    ans = []
    ans = q.quick_sort(inp,0, len(inp)-1)
    ans = ans[-3:]
    print(ans)
    return ans


def test_find_k_largest():
    inp = [1,5,7,8,4,2,3,6]
    k = 3
    ans = [6,7,8]
    assert(find_k_largest(inp, 3) == ans)
    print('테스트 통과!')


if __name__ == '__main__':
    test_find_k_largest()