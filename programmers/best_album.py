from collections import OrderedDict

def solution(genres, plays):
    ans = []
    gp_dic = {}

    for i, gp in enumerate(zip(genres, plays)):
        gp_dic[i] = gp
    # print(gp_dic)

    s = set(genres)
    d = dict()
    for item in s:
        d[item] = 0

    for key, val in gp_dic.items():
        # print(val)
        if val[0] in s:
            d[val[0]] += val[1]

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print('\n', d)

    s1 = map(lambda x: x[0], d)
    dic_lst = [{} for i in range(len(d))]
    # print(dic_lst)
    
    dic_dic = OrderedDict()
    for key in s1:
        dic_dic[key] = {}
    # print(dic_dic)

    for item in gp_dic.items():
        # print(item, type(item))
        if item[1][0] in s:
            dic_dic[item[1][0]][item[0]] = item[1]
    # print(dic_dic)

    res = []

    for key, val in dic_dic.items():
        # print(key, val, type(val))
        val = sorted(val.items(), key=lambda x: x[1][1], reverse=True)
        # print(dict(val))
        res.append(dict(val))

    # print(res)

    for item in res:
        cnt = 1
        for key in item.keys():
            if cnt <= 2:
                ans.append(key)
            cnt+=1
    # print(ans)


    return ans


def test(genres, plays, ans):
    try:
        assert len(genres) >= 1 and len(genres) <= 10000 and len(genres) == len(plays)
        assert len(set(genres)) < 100
        assert(solution(genres, plays) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500], [4,1,3,0])