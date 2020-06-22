# 단순 탐색

## 장점
# 정렬이 안되있어도 됨

## 단점
# 느림, O(n)

## 대안
# 이진탐색, O(log n)

def search(arr, target):
    for idx in range(0, len(arr)):
        if arr[idx] == target:
            return idx
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(search(arr, 9))