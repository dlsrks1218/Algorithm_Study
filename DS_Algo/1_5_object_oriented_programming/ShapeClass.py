import math

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # 메서드 속성
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)
        
    def __eq_(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return 'point ({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!r}, {0.y!r})'.format(self)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        # 생성 및 초기화
        self.radius = radius
        super().__init__(x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius**2)
    
    # circumference : 둘레
    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return 'circle ({0.radius!r}, {0.x!r})'.format(self)

    def __str__(self):
        return repr(self)
    

import ShapeClass as shape

a = shape.Point(3, 4)
print(a)
print(repr(a))
print(str(a))
print(a.distance_from_origin())
print()

c = shape.Circle(3,2,1)
print(c)
print(repr(c))
print(str(c))
print(c.circumference())
print(c.edge_distance_from_origin())