import time

# 단순한 퀵정렬 구현이 가능하지만 재귀호출이 일어날 때마다 새로운 리스트가 생성되어 비효율적
def qs1(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]
    smaller, equal, bigger = [], [], []
    for num in lst:
        if num < pivot:
            smaller.append(num)
        if num == pivot:
            equal.append(num)
        if num > pivot:
            bigger.append(num)
    return qs1(smaller) + equal + qs1(bigger)

def qs2(lst):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        # 퀵정렬에서 피벗을 기준으로 나뉜 리스트 갯수가 비슷할수록 성능이 좋다
        # 따라서 중앙값을 피벗으로 사용
        pivot = lst[(low+high)//2]
        while low <= high:
            while lst[low] < pivot:
                low += 1
            while lst[high] > pivot:
                high -= 1
            if low <= high:
                lst[low], lst[high] = lst[high], lst[low]
                low, high = low + 1, high - 1
        return low
    
    return sort(0, len(lst)-1)

def qs3(lst, low, high):
    def partition(low, high):
        # 퀵정렬에서 피벗을 기준으로 나뉜 리스트 갯수가 비슷할수록 성능이 좋다
        # 따라서 중앙값을 피벗으로 사용
        pivot = lst[(low+high)//2]
        while low <= high:
            while lst[low] < pivot:
                low += 1
            while lst[high] > pivot:
                high -= 1
            if low <= high:
                lst[low], lst[high] = lst[high], lst[low]
                low, high = low + 1, high - 1
        return low
    
    if low >= high:
        return
    mid = partition(low, high)
    qs3(lst, low, mid - 1)
    qs3(lst, mid, high)
    
    return lst

def qs4(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [num for num in arr[1:] if num <= pivot]
    greater = [num for num in arr[1:] if num > pivot]
    # print(less, greater)

    return qs4(less) + [pivot] + qs4(greater)


lst = [5,4,8,6,1,3,2,7]

# start1 = time.time()
# print(qs1(lst), time.time() - start1)

# start2 = time.time()
# qs2(lst)
# print(lst, time.time() - start2)

# print(qs3(lst, 0, len(lst)-1))

print(qs4(lst))