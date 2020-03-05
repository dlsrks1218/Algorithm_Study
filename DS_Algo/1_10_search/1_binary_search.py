def binary_search_recursion(inp, target, low, high):
    '''
    이진 탐색(재귀함수)을 통해 target의 위치를 반환
    시간 복잡도 : O(nlogn)
    '''
    if low > high:
        return None
    mid = (low + high) // 2
    if target == inp[mid]:
        return mid
    elif target < inp[mid]:
        return binary_search_recursion(inp, target, low, mid-1)
    else:
        return binary_search_recursion(inp, target, mid+1, high)


def binary_search_iter(inp, target):
    '''
    이진 탐색(반복문)을 통해 target의 위치를 반환
    시간 복잡도 : O(nlogn)
    '''
    low, high = 0, len(inp)
    while low < high:
        mid = (low + high) // 2
        if target == inp[mid]:
            return mid
        elif target < inp[mid]:
            high = mid
        else:
            low = mid + 1
    return None


def test_binary_search():
    inp = [0,3,5,4]
    target = 5
    assert(binary_search_recursion(inp, target, 0, len(inp)) == 2)
    assert(binary_search_iter(inp,target) == 2)
    print('테스트 통과!')


if __name__ == '__main__':
    test_binary_search()