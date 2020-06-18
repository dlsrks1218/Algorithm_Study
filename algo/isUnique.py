def solution(arr):
    groupby = list(set(arr))
    result = dict()
    for item in groupby:
        result[item] = arr.count(item)

    answer = []
    
    for v in result.values():
        if v != 1:
            answer.append(v)
    
    if not len(answer):
        return [-1]

    return answer

print(solution([3,5,7,9,1]))
print(solution([1,2,3,3,3,3,4,4]))
print(solution([3,2,4,4,2,5,2,5,5]))