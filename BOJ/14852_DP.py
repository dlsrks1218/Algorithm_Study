# def dp(x):
#     memo = [0]*(x + 1)

#     if x == 0:
#         return 1
#     if x == 1:
#         return 2
#     if x == 2:
#         return 7
#     if memo[x] != 0:
#         return memo[x]
#     else:
#         res = 2 * dp(x-1) + 3 * dp(x-2)
#         for i in range(3, x+1):
#             res += (2 * dp(x - i)) % 1000000007
#         memo[x] = res % 1000000007
#     return memo[x]


def dp(x):
    memo = [[0 for col in range(2)] for row in range(x+1)]
    memo[0][0] = 0
    memo[1][0] = 2
    memo[2][0] = 7
    memo[2][1] = 1
    for i in range(3, x + 1):
        memo[i][1] = (memo[i-1][1] + memo[i-3][0]) % 1000000007
        memo[i][0] = (3 * memo[i-2][0] + 2 * memo[i-1][0] + 2 * memo[i][1]) % 1000000007
    return memo[x][0]


if __name__ == '__main__':
    x = int(input())
    print(dp(x))