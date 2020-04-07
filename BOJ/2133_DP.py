def dp(x):
    d = [0]*(x + 1)

    if x == 0:
        return 1
    if x == 1 or x % 2 != 0:
        return 0
    if x == 2:
        return 3
    if d[x] != 0:
        return d[x]
    else:
        res = 3 * dp(x - 2)
        # for i in range(3, x + 1):
        #     if i % 2 == 0:
        #         res += 2 * dp(x - i)
        # d[x] = res

        for i in range(4, x+1, 2):
            res += 2 * dp(x-i)
        d[x] = res
    return d[x]

if __name__ == '__main__':
    x = int(input())
    print(dp(x))