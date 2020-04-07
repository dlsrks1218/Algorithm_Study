def dp(x):
    memo = [0]*100
    if x == 1 or x == 2:
        return 1
    if memo[x] != 0:
        return memo[x]
    else:
        memo[x] = dp(x-1) + dp(x-2)
    return memo[x]

if __name__ == '__main__':
    x = int(input())
    print(dp(x))