n = int(input())

a = list(map(int, input().split()))

# print(n, a)

# def reverse(x):
#     tmp = str(x)
#     if tmp[-1] == '0':
#         tmp[-1].replace('')
#     return int(tmp[::-1])

# def is_prime(x):
#     if x % 10:
#         pass
#     else:
#         reverse(x)

# b = list(map(reverse, a))
# print(b)


def reverse(x):
    res = 0
    while x>0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    # 1은 소수가 아니므로 False 리턴 > 함수 종료
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            # x는 i의 약수
            return False
    else:
        #정상적으로 종료되었다면
        return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')