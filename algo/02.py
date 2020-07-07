def toSet(arr):
    answer = []
    for idx, num in enumerate(arr):
        if num not in arr[idx+1:]:
            answer.append(num)
    return answer

def sum(base, other):
    answer = base.copy()
    for other_num in other:
        if other_num in base:
            continue
        else:
            answer.append(other_num)
    return answer

def complement(base, other):
    answer = []
    for base_num in base:
        if base_num not in other:
            answer.append(base_num)
    return answer

def intersect(base, other):
    answer = []
    for base_num in base:
        if base_num in other:
            answer.append(base_num)
    return answer


arrA = [1,2,3,2]
arrB = [1,3]

# arrA = [2,3,4,3,5]
# arrB = [1,6,7]

def solution(arrA, arrB):
    answer = []

    arrA_set = toSet(arrA)
    arrB_set = toSet(arrB)

    sum_res = sorted(sum(arrA_set, arrB_set))
    comp_res = sorted(complement(arrA_set, arrB_set))
    inter_res = sorted(intersect(arrA_set, arrB_set))
    
    print('A 집합 =', arrA_set)
    print('B 집합 =', arrB_set)
    print('합집합sum =', sum_res)
    print('차집합complement =', comp_res)
    print('교집합intersect =', inter_res)

    answer.append(len(arrA_set))
    answer.append(len(arrB_set))
    answer.append(len(sum_res))
    answer.append(len(comp_res))
    answer.append(len(inter_res))

    return answer

def test(arrA, arrB):
    try:
        assert len(arrA) >= 0 and len(arrA) <= 1000000
        # print(solution(arrA, arrB))
        solution(arrA, arrB)
    except AssertionError as err:
        print('값을 다시 입력해주세요')

if __name__ == '__main__':
    test(arrA, arrB)