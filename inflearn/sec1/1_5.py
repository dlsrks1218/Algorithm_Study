n, m = map(int, input().split())
# print(n, m)

cnt = [0]*(n+m+3)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

max = -2147000000

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')
# matrix = [[0 for col in range(m)] for row in range(n)]
# for line in matrix:
#     print(line)
# print()

# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i+1 + m+1

# for line in matrix:
#     print(line)
