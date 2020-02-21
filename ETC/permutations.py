from itertools import permutations

def solution(n, r):
    ans = []
    alpha = []
    
    for i in range(0, n):
        alpha.append(chr(ord('a')+i))
    
    print(alpha)
    print(list(permutations(alpha, 2)))
    return list(permutations(alpha, 2))

solution(4, 2)