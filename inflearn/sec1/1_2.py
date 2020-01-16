# k번째 작은 수, n개의 수 중 s번째부터 e번째까지 수 중 k번째 작은 수 
import sys

sys.stdin = open('/Users/jonghyunlim/Documents/Project/Algorithm/inflearn/AA/1_2_input.txt', 'rt')
T = int(input())
for i in range(T):
    n, s, e, k = map(int, input().split())
    # print(n,s,e,k)
    a = list(map(int, input().split()))
    # print(a)
    a = a[s-1:e]
    # print(a)
    a.sort()
    # print(a)
    print('#%d %d' %(i+1, a[k-1]))