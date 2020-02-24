# 이진 검색 알고리즘(binary search algorithm)은 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이며, 
# 처음 중간의 값을 임의의 값으로 선택하여, 그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식을 채택하고 있다. 
# 처음 선택한 중앙값이 만약 찾는 값보다 크면 그 값은 새로운 최고값이 되며, 작으면 그 값은 새로운 최하값이 된다.

# 정렬된 정수배열에서 Binary Search를 이용하여 제시된 숫자들을 찾아라. 
# 있으면 해당 인덱스를 출력하고, 없으면 -1 를 출력하라. (2 ≤ M ≤ 100)

# 2 // # of test case T
# 12 // # of element in array M
# 5 // # of numbers to search N
# 3 7 28 29 43 49 55 58 69 77 79 99 // sorted integer array
# 8 49 58 44 7 // numbers to search
# 7
# 3
# 3 4 5 6 7 8 9
# 1 2 3

def binary_search(sarr, low, high, target):
    mid = 0
    if low > high:
        print(' -1', end='')
        return
    mid = int((low + high) / 2)
    if target < sarr[mid]:
        binary_search(sarr, low, mid - 1, target)
    elif sarr[mid] < target:
        binary_search(sarr, mid + 1, high, target)
    else:
        print(' %d' %(mid), end='')
        return

T = int(input())

for i in range(T):
    M = int(input())
    N = int(input())
    sorted_arr = list(map(int, input().split()))
    target_arr = list(map(int, input().split()))
    
    print('#%d' %(i+1), end='')
    
    for i in range(N):
        binary_search(sorted_arr, 0, M-1, target_arr[i])
