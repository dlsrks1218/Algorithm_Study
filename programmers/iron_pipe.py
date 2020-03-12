def solution(arrangement):
    ans = 0
    arrangement = arrangement.replace('()', 'l')

    pipe = 0

    for idx, ch, in enumerate(arrangement):
        if (idx == 0 or idx == len(arrangement)-1) and ch == 'l':
            pass
        if ch == '(':
            pipe+=1
        if ch == ')':
            ans+=1
            pipe-=1
        if ch == 'l':
            ans+=pipe
    # print(ans)
    return ans
    
# def solution(arrangement):
#     ans = 0
#     dic = dict()

#     for i in range(len(arrangement)):
#         dic[i] = arrangement[i]    

#     # print(dic)

#     pipe_lst = []
#     pipe_start = []
#     pipe_end = []
#     laser_lst = []
    
#     pipe = []

#     for key in dic.keys():
#         tmp = dic.get(key)
#         pipe.append(tmp)
        
#         if tmp == '(':
#             if dic.get(key+1) == ')':
#                 laser_lst.append(key+1)
#             # if dic.get(idx+1) != ')'
#             else:
#                 pipe_start.append(key)
        
#         if tmp == ')' and pipe[-2] == '(':
#             pipe.pop()
#             pipe.pop()
#             if key not in laser_lst:
#                 pipe_end.append(key)
        
#     print(laser_lst)
    
#     for s, e in zip(pipe_start, pipe_end):
#         pipe_lst.append(range(s, e))

#     print(pipe_lst)
    
#     for pipe in pipe_lst:
#         cnt = 0
#         for laser in laser_lst:
#             if laser in pipe:
#                 cnt += 1
#         ans += cnt+1
#     # print(ans)
#     return ans


def test(arrangement, ans):
    try:
        assert len(arrangement) <= 100000
        assert(solution(arrangement) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test('()(((()())(())()))(())', 17)