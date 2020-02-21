def reverse(x):
    res = 0
    while x>0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

print(reverse(9010))
