def solution(dartResult):
    score_lst = []
    cnt = 0
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            pass
        elif dartResult[i] == 'D':
            score_lst[cnt-1] = score_lst[cnt-1] ** 2
        elif dartResult[i] == 'T':
            score_lst[cnt-1] = score_lst[cnt-1] ** 3
        elif dartResult[i] == '*':
            score_lst[cnt - 1] = score_lst[cnt - 1] * 2
            if cnt>1:
                score_lst[cnt - 2] = score_lst[cnt - 2] * 2
        elif dartResult[i] == '#':
            score_lst[cnt-1] = score_lst[cnt-1] * -1
        else:
            if dartResult[i+1] == '0':
                score_lst.append(10)
                i+=1
            else:
                score_lst.append(int(dartResult[i]))
            cnt+=1
    print(sum(score_lst))
    return sum(score_lst)
solution("1D2S#10S")