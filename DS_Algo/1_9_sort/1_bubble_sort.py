def bubble_sort(inp):
    answer = []
    for num in range(len(inp)-1, 0, -1):
        print(inp[num], inp)
        for i in range(num):
            if inp[i] > inp[i+1]:
                inp[i], inp[i+1] = inp[i+1], inp[i]
    answer = inp
    return answer


def test_bubble_sort():
    inp = [1,4,3,2,5]
    ans = [1,2,3,4,5]
    assert(bubble_sort(inp) == ans)
    print('테스트 통과!')


if __name__ == '__main__':
    test_bubble_sort()
    # bubble_sort([1,4,3,2,5])