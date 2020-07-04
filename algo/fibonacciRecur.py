# fib(1) = 1, fib(2) = 2, fib(3) = 2, fib(4) = 3

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(100))