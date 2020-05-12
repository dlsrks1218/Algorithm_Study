# from collections import defaultdict, deque

# def solution(k, room_num):
#     ans = []

#     # available = dict()
#     # for i in range(1, k+1):
#     #     available[i] = 0
#     # print(available, room_num)

#     # deq = deque(room_num)
    
#     # for num in room_num:
#     #     if num in available.keys():
#     #         available[num] = 1
#     #         ans.append(room_num.pop(0))
#     #         available.pop(num)
#     #     print(available, ans, room_num)
#     #     if num not in available.keys():

#     #     # if num not in         


#     available = [i for i in range(1, k+1)]
#     for num in room_num:
#         if num in available:
#             ans.append(num)
#     print(ans)

#     return ans

import sys
sys.setrecursionlimit(10000000) # 설정해주지 않으면 재귀가 많이 일어나면서 런타임에러 등이 나타날 수 있다.

def findEmptyRoom(number, rooms): # 빈방을 찾는 함수
    if number not in rooms:        
        rooms[number] = number + 1
        return number
    
    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    rooms = dict() # 몇번 방이 비어있는지 체크하는 딕셔너리

    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)
    
    return answer
    
def test(k, room_num, ans):
    try:
        assert k >= 1 and k <= 10**12
        assert len(room_num) >= 1 and len(room_num) <= 200000
        assert list(filter(lambda x: x>=1 and x<=k, room_num))
        assert(solution(k, room_num) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test(10, [1,3,4,1,3,1], [1,3,4,2,5,6])