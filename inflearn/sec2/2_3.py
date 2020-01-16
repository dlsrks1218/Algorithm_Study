# input
# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20

card = [i for i in range(1, 21)]

def reverse(s, e, card):
    tmp = card[s-1:e]
    reverse_tmp = []

    # tmp = tmp[::-1]
    for i in range(len(tmp)-1, -1, -1):
        print(tmp[i])
        reverse_tmp.append(tmp[i])
    
    card[s-1:e] = reverse_tmp
    return card

com_lst = []

for i in range(10):
    se = list(map(int, input().split()))
    com_lst.append(se)

for com in com_lst:
    card = reverse(com[0], com[1], card)

print(card)