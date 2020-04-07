def dp(x):
    memo = [0]*1001
    if x==1:    
        return 1
    if x==2:    
        return 3
    if memo[x] != 0:
        return memo[x]
    else:
        memo[x] = (dp(x-1) + 2 * dp(x-2)) % 10007
    return memo[x]

if __name__ == '__main__':
    x = int(input())
    print(dp(x))