from collections import defaultdict, OrderedDict

def solution(strings, n):
    ans = []
    
    tmp = dict()
    tmp_set = set()
    dic = {}
    
    for idx, string in enumerate(strings):
        tmp[idx] = string[n]
        tmp_set.add(string[n])
    # print(tmp,tmp_set)

    for item in tmp_set:
        dic[item] = []
    # print(dic)

    res = OrderedDict(sorted(dic.items()))
    # print(res)

    for key, val in tmp.items():
        res[val].append(key)
    # print(res)

    for key, val in res.items():
        cur_list = {}
        for idx in val:
            cur_list[idx] = strings[idx]
        cur_list = sorted(cur_list.items(), key = lambda item: item[1])
        # print(cur_list)
        for item in cur_list:
            ans.append(item[1])

    return ans


def test(strings, n, ans):
    try:
        assert len(strings) >= 1 and len(strings) <= 50
        assert lambda item: len(item) >= 1 and len(item) <= 100 and len(item) > n, strings
        assert(solution(strings, n) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test(['sun', 'bed', 'car'], 1, ['car', 'bed', 'sun'])
    test(['sun', 'bed', 'car', 'tar'], 1, ['car', 'tar', 'bed', 'sun'])
    test(['abce', 'abcd', 'cdx'], 2, ['abcd', 'abce', 'cdx'])