def binary_search_iter(inp, target):
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

#binary_search_iter(inp,target)