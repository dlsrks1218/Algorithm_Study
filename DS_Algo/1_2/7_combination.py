from itertools import combinations

def combi(s):
    if len(s) < 2:
        return s
    res = []
    
    for i, c in enumerate(s):
        res.append(c)
        for cc in combi(s[:i] + s[i+1:]):
            res.append(c + cc)

    return res
    

if __name__ == '__main__':
    s = '012'
    print(combi(s))