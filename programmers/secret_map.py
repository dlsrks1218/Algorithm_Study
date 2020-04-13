# def convert(n, base):
#     T = "0123456789ABCDEF"
#     q, r = divmod(n, base)
#     if q == 0:
#         return T[r]
#     else:
#         return convert(q, base) + T[r]


# def solution(n, arr1, arr2):
#     answer = []
#     arr3, arr4 = [], []
#     for num1, num2 in zip(arr1, arr2):
#         arr3.append(convert(num1, 2))
#         arr4.append(convert(num2, 2))
#     print(arr3)
#     print(arr4)
#     return answer

# solution(5, [9,20,28,18,11], [30,1,21,17,28])


def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a = str(bin(a1 | a2))[2:]
        a = '0' * (n - len(a)) + a
        print(a)
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        answer.append(a)

    print(answer)
    return answer

solution(5, [9,20,28,18,11], [30,1,21,17,28])