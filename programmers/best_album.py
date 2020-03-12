from collections import Counter
from collections import OrderedDict


def solution(genres, plays):
    ans = []
    gp_dic = {}

    for i, gp in enumerate(zip(genres, plays)):
        gp_dic[i] = gp

    print(gp_dic)

    res = sorted(gp_dic.items(), key = lambda item: item[1][0])
    print(res)
    # res = sorted(gp_dic.items(), key = lambda item: item[1][1])
    # print(res)

    g = set(genres)
    print(g)
    g_l = {}
    for item in res:
        # print(list(item)[1][0], list(item)[1][1])
        if list(item)[1][0] in g:
            g_l[list(item)[1][0]] += list(item)[1][1]
    print(g_l)


    

    # # 장르별로 소팅
    # res = sorted(gp_dic.items(), key = list(gp_dic.values())[0])
    # # 재생 횟수 별로 소팅
    # res = sorted(gp_dic.items(), key = list(gp_dic.values())[1])
    # print(res)
    
    
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