def pick2(arr):
    list = []
    list.append((arr[0], arr[1])) # tuple
    list.append((arr[0], arr[2]))
    list.append((arr[0], arr[3]))
    list.append((arr[0], arr[3]))
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            list.append((arr[i], arr[j]))
    return list

# arr = [1, 2, 3, 4, 5, 6, 7]
# arr = [i for i in range(0, 8)]
arr = [i+1 for i in range(0, 7)]
print(arr)

print(pick2(arr))

# 7C2 = 21