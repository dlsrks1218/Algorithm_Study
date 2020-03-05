def partition(inp, start, end):
    '''두 함수로 나누어 구현 (캐시 사용X)'''
    pivot = inp[start]
    left = start+1
    right = end
    done = False

    while not done:
        while left <= right and inp[left] <= pivot:
            left += 1
        while left <= right and pivot < inp[right]:
            right -= 1
        if right < left:
            done = True
        else:
            inp[left], inp[right] = inp[right], inp[left]
    inp[start], inp[right] = inp[right], inp[start]
    print(right, inp)
    
    return right


def quick_sort(inp, start, end):
    ans = []
    if start < end:
        pivot = partition(inp, start, end)
        quick_sort(inp, start, pivot-1)
        quick_sort(inp, pivot+1, end)
    ans = inp

    return ans


# def test_quick_sort():
#     inp = [1,7,4,5,3,2,6]
#     ans = [1,2,3,4,5,6,7]
#     assert(quick_sort(inp,0, len(inp)-1) == ans)
#     print('테스트 통과!')