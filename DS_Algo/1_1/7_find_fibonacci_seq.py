import math

# O(n)
def find_fibonacci_seq_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# O(2**n)
def find_fibonacci_seq_rec(n):
    if n < 2:
        return n
    return find_fibonacci_seq_rec(n-1) + find_fibonacci_seq_rec(n-2)

def test():
    n = 10
    assert(find_fibonacci_seq_iter(n) == 55)
    assert(find_fibonacci_seq_rec(n) == 55)
    print('test pass')


if __name__ == '__main__':
    test()