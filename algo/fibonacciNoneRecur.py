# 패턴 찾기(단순 접근) -> 최적화(반복 횟수 줄이기)
# fib(1) = [1], fib(2) = [1, 2]

def fib(n):
    result = []
    if n <= 1:
        return [1]
    first, second = 1, 1

    result.append(first)
    result.append(second)
    
    for i in range(2, n):
        print(first, second)
        third = first + second
        result.append(third)
        first = second
        second = third

    return result.pop()


print(fib(3))
