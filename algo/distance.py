import math

# 클래스를 좌표로 사용
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getDistance1(p1, p2):
    return math.sqrt(math.pow((p1.x-p2.x), 2) + math.pow((p1.y-p2.y), 2))
    # return math.sqrt(((p1.x - p2.x)**2) + abs((p1.y - p2.y)**2))

p1 = Point(0, 0)
p2 = Point(2, 2)
print(getDistance1(p1, p2))

# 튜플을 좌표로 사용
def getDistance2(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

print(getDistance2((0,0), (2, 2)))