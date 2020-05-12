def convert(num):
    line1 = [1, 2, 3]
    line2 = [4, 5, 6]
    line3 = [7, 8, 9]
    line4 = ['*', 0, '#']

    if num in line1:
        return 1
    elif num in line2:
        return 2
    elif num in line3:
        return 3
    elif num in line4:
        return 4


def solution(numbers, hand):
    answer = ''

    # line1 = {1: [1, 2, 3]}
    # line2 = {2: [4, 5, 6]}
    # line3 = {3: [7, 8, 9]}
    # line4 = {4: ['*', 0, '#']}

    left = [1, 4, 7]
    right = [3, 6, 9]
    mid = [2, 5, 8, 0]
    h = ''
    f1, f2 = '*', '#'

    if hand == 'right':
        h += 'R'
    else:
        h += 'L'

    for num in numbers:
        if num % 3 == 1: # L
            f1 = num
            answer += 'L'
        elif num % 3 == 0: # R
            f2 = num
            answer += 'R'
        elif num % 3 == 2: # M
            dif1 = convert(num) - convert(f1)
            dif2 = convert(num) - convert(f2)
            if dif1 == 0:
                dif1 = abs(num - f1)
            elif dif2 == 0:
                dif2 = abs(num - f2)
            else:
                if abs(dif1) > abs(dif2):
                    f2 = num
                    answer += 'R'
                elif abs(dif1) < abs(dif2):
                    f1 = num
                    answer += 'L'
                else: # ==
                    answer += h
                    if h == 'L':
                        f1 = num
                    elif h == 'R':
                        f2 = num

    return answer

print('13458214595')
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print("LRLLLRLLRRL")
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right" , "LRLLLRLLRRL"))

print()
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
print("LLRLLRLLRL")