def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

def solution(num):
    for i in range(num):
        case = int(input())
        print(factorial(case))
        
n = int(input())
solution(n)    

