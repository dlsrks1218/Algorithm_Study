progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    ans = []
    days_left = []
    for p, s in zip(progresses, speeds):
        cnt=0
        while p<100:
            p+=s
            cnt+=1
        days_left.append(cnt)
    
    # print(days_left)
    
    cnt=1
    
    for i in range(len(days_left)):
        if i<len(days_left)-1:
            if days_left[i] < days_left[i+1]:
                ans.append(cnt)
                cnt=1
            else:
                days_left[i+1] = days_left[i]
                cnt+=1
            ans.append(cnt)
    
    print(ans)
    return ans
# def solution(progresses, speeds):
#     ans = []
#     stk = []
#     for idx, p in enumerate(progresses):
#         cnt = 0
#         while p<100:
#             p+=speeds[idx]
#             cnt+=1
#         stk.append(cnt) 
    
#     tmp = list(sorted(stk))
#     for idx, t in enumerate(tmp):
#         if t == stk[0]:
#             ans.append(len(tmp[:idx+1]))
#         if t > stk[0]:
#             ans.append(1)
#     print(ans)
#     return ans

solution(progresses, speeds)