n = int(input())

a = list(map(int, input().split()))
b = [0]*n

for i in range(len(a)):
    if i==0:
        if a[i]==1:
            b[i] = 1
    else:   #i!=0
        if a[i]==1:
            if a[i] == a[i-1]:
                b[i] = b[i-1]+1
            else: 
                b[i] = 1

# print(b)
print(sum(b))

## input
# 10
# 1 0 1 1 1 0 0 1 1 0