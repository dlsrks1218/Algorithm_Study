n = int(input())

lst = list(map(int, input().split()))
res_lst = []

def digit_sum(x):
    dsum = 0
    tmp = str(x)
    for ch in tmp:
        dsum+=int(ch)
    return dsum

for x in lst:
    res_lst.append(digit_sum(x))

print(lst[res_lst.index(max(res_lst))])
