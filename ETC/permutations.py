from itertools import permutations

def solution(n, r):
    ans = []
    alpha = []
    
    for i in range(0, n):
        alpha.append(chr(ord('a')+i))
    
    print(alpha)
    ans = list(permutations(alpha, 2))
    print(ans)
    return ans

solution(4, 2)