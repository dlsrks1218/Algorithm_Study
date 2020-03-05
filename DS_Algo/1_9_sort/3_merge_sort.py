def merge_sort(inp):
    '''pop()을 이용한 병합정렬'''
    if len(inp) < 2:
        return inp
    
    mid = len(inp)//2
    left, right = inp[:mid], inp[mid:]

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    ans = []
    while left and right:
        if left[-1] >= right[-1]:
            ans.append(left.pop())
        else:
            ans.append(right.pop())
    ans.reverse()
    print(ans)
    
    return (left or right) + ans


def test_merge_sort():
    inp = [1,5,4,2,3,9,6]
    ans = [1,2,3,4,5,6,9]
    assert(merge_sort(inp) == ans)
    print('테스트 통과!')


if __name__ == '__main__':
    test_merge_sort()