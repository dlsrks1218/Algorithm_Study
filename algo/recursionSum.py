def recur_sum(arr, result):
    # 종료 조건
    if not arr:
        return result
    last = arr.pop()
    result += last    

    return recur_sum(arr, result)

arr = [1,3,5,7]
print(recur_sum(arr, 0))