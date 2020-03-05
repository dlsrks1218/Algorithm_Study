# n번째 피보나치 수열 구하기
def find_fibo_seq(n):
    if n < 2:
        return n
    return find_fibo_seq(n-1) + find_fibo_seq(n-2)


if __name__ == '__main__':
    print(find_fibo_seq(5))