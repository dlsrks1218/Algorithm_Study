from collections import OrderedDict

def solution(answers):
    # answer = 0
    # return answer
    ans = []

    way_answersheet = OrderedDict()
    way_answersheet[1] = [1,2,3,4,5]
    way_answersheet[2] = [2,1,2,3,2,4,2,5]
    way_answersheet[3] = [3,3,1,1,2,2,4,4,5,5]
    # print(way_answersheet)

    alen = len(answers)

    for key, way in way_answersheet.items():
        if len(way) < alen:
            way_answersheet[key] = (way * (alen//len(way)+1))[:alen]
        if len(way) >= alen:
            way_answersheet[key] = way[:alen]
    
    # print(way_answersheet)

    cnt_dic = OrderedDict()
    cnt_dic = {1:0, 2:0, 3:0}
    
    for key, way in way_answersheet.items():
        for pair in zip(way, answers):
            if pair[0] == pair[1]:
                cnt_dic[key]+=1
    
    # print(cnt_dic)

    res = dict(sorted(cnt_dic.items(), key=lambda x:x[1], reverse=True))

    # print(res)

    max_val = max(res.values())

    for k, v in res.items():
        if v == max_val:
            ans.append(k)
    
    # print(ans)
    return ans


if __name__ == '__main__':
    # solution([1,2,3,4,5,2,4])
    solution([1,3,2,4,2])
    # solution([3,3,2,4,1])
    # solution([5,5,5,5,2])