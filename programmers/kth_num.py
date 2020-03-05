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
    # print(right, inp)
    
    return right


def quick_sort(inp, start, end):
    # quick_sort(inp,0, len(inp)-1)
    ans = []
    if start < end:
        pivot = partition(inp, start, end)
        quick_sort(inp, start, pivot-1)
        quick_sort(inp, pivot+1, end)
    ans = inp

    return ans


def solution(arr, coms):
    # i, j, k = coms[0][0], coms[0][1], coms[0][2]
    # print(arr[i-1:j])
    answer = []
    for i,j,k in coms:
        tmp_arr = arr[i-1:j]
        # print(quick_sort(tmp_arr, 0, len(tmp_arr)-1), quick_sort(tmp_arr, 0, len(tmp_arr)-1)[k-1])
        answer.append(quick_sort(tmp_arr, 0, len(tmp_arr)-1)[k-1])

    # print(answer)
    return answer


if __name__ == '__main__':
    solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]])