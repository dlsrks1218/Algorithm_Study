n,m = map(int, input().split())

num_lst = list(map(int, input().split()))

# print(num_lst)

cnt = 0

for i in range(len(num_lst)-1):
    tmp = num_lst[i]
    while tmp != m:
        tmp += num_lst[i+1]
        if tmp == m:
            cnt += 1
            break
    
    # for j in range(i+1, len(num_lst)):
    #     if tmp == m:
    #         cnt += 1
    #         break
    #     tmp += num_lst[j]
        # print(tmp)

print(cnt)