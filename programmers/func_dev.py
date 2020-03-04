def solution(progresses, speeds):
    ans = []
    days_left = []
    
    for p, s in zip(progresses, speeds):
        cnt=0
        while p<100:
            p+=s
            cnt+=1
        days_left.append(cnt)
    print(days_left)

    cnt = 1
    for i in range(len(days_left)-1):
        if days_left[i] < days_left[i+1]:
            ans.append(cnt)
            cnt=1
        else:
            days_left[i+1] = days_left[i]
            cnt+=1
        if i == len(days_left)-2:
            ans.append(cnt)
        
    print(ans)
    return ans

# solution([93,30,55], [1,30,5])
solution([93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7])