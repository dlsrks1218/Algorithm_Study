import random

class Player:
    def __init__(self, num=0):
        self.num = num

    def play(self):
        s = [str(random.randrange(1,10))*3]
        self.num = int(''.join(s))

    def guess(self):
        s = [str(random.randrange(1,10))*3]
        gnum = int(''.join(s))

        return gnum


def solution(inp1):
    ans = 0

    p1, p2 = Player(), Player()

    p1.play()
    p2.play()

    print(p1.num, p2.num)
    cnt = 0
    while True:
        cnt+=1
        if p1.guess() == p2.num:
            print(cnt+1,'번 만에 p1 승리')
            break
        elif p2.guess() == p1.num:
            print(cnt+1,'번 만에 p2 승리')
            break
        
    return ans


def test(inp1, ans):
    try:
        assert len(inp1) >= 1 and len(inp1) <=100
        assert(solution(inp1) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]], 2)