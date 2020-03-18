'''
int 형 리스트를 join 하려면 아래와 같이 모든 요소를 str으로 바꾸어야함
print(" ".join(map(str, num_list)))
'''

# from itertools import permutations

# def solution(inp):
    # ans = 0
    # item_lst = list(map(lambda x: ''.join(map(str, x)), list(permutations(inp))))
    # ans = sorted(item_lst)[-1]

    # return str(ans)

# def solution(inp):
#     ans = ''
#     idx_lst = []
#     dic = dict()

#     for item in inp:
#         if len(str(item)) != 1:
#             dic[item//(10**(len(str(item))-1))] = item
#         else:
#             dic[item] = item
#     print(dic)

#     dic = sorted(dic.items(), key = lambda x: x[0], reverse=True)
#     # print(dic)
#     ans_lst = list(map(lambda x: x[1], dic))
#     ans = str(ans.join(map(str, ans_lst)))
        
#     print(ans)
#     return ans

# def solution(inp):
#     ans = ''
#     idx_lst = []
#     dic = dict()

#     for item in inp:
#         if len(str(item)) != 1:
#             dic[item] = item//(10**(len(str(item))-1))
#         else:
#             dic[item] = item
#     print(dic)

#     dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
#     print(dic)
#     ans_lst = list(map(lambda x: x[0], dic))
#     ans = str(ans.join(map(str, ans_lst)))
        
#     print(ans)
#     return ans


def solution(inp):
    inp = list(map(str, inp))
    # print(inp)
    inp.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(inp)))


def test(inp, ans):
    try:
        assert len(inp) >= 1 and len(inp) <= 100000
        assert min(inp)>= 0 and max(inp) <= 1000
        assert(solution(inp) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test([6,10,2], '6210')
    test([3, 30, 34, 5, 9], '9534330')