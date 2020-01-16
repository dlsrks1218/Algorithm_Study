T = int(input())

T_lst = []

for i in range(T):
    n, s, e, k = map(int, input().split())
    n_lst = list(map(int, input().split()))
    n_lst = n_lst[s-1:e]
    n_lst.sort()
    print('#%d %d' %(i+1, n_lst[k-1]))

# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15