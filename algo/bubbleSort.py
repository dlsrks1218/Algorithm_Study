def bs(arr):
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

arr = [7,3,2,9,4]
print(bs(arr))
print(arr)