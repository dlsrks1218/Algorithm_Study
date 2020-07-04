"""
피보나치 수열(다이나믹 프로그래밍)
- Dynamic Programming
- Memoization
    - 결과값을 메모
    - 함수 호출 비용은 크다
    - 함수 호출을 적게 하기 위한 방법
    - 메모 해놓은 값을 넘겨 이미 계산된 값은 다시 계산하지 않음
"""

def fib(n, memo):
    if n <= 1:
        return n
    # memo[n]이 없을때(None일때) 계산해서 넣는 로직
    if memo[n] is None:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    # targetValue = memo[n] # target[n]
    # print('targetValue:', targetValue)

    return memo[n]

num = 10
memo = [None] * (num+1)
print(fib(num, memo))