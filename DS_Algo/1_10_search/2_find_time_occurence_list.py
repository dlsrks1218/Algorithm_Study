import binary_search as bs

def find_k_occur(inp, k):
    '''
    리스트에서 타겟(k)가 등장하는 횟수 구하기
    '''
    cnt = 1
    idx = bs.binary_search_iter(inp, k)
    for i in range(idx+1, len(inp)):
        if inp[i] == k:
            cnt += 1
        else:
            break
    for i in range(idx-1, -1, -1):
        if inp[i] == k:
            cnt += 1
        else:
            break
    return cnt


def test_find_k_occur():
    inp = [1,2,2,2,2,2,2,5,6,6,7,8,9]
    k = 2
    assert(find_k_occur(inp, k) == 6)
    print('테스트 통과!')


if __name__ == '__main__':
    test_find_k_occur()