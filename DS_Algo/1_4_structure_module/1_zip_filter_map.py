print('zip()')
a = [1,2,3,4,5]
b = ['a', 'b', 'c', 'd']
print(zip(a,b))
print(list(zip(a,b)))
print()

print('filter()')
def f(x): return x % 2 != 0 and x % 3 != 0
print(f(33), f(17))
print(list(filter(f, range(2, 25))))
print()

print('map()')
def cube(x): return x * x * x
print(list(map(cube, range(1, 11))))
seq = range(8)
def square(x): return x * x
print(list(zip(seq, map(square, seq))))
print()

print('lambda function')
# def area(b, h): return 0.5 * b * h
# print(area(5, 4))
area = lambda b, h: 0.5 * b * h
print(area(5, 4))
print()

print('lambda func to initiate defaultdict')
from collections import defaultdict
minus_one_dict = defaultdict(lambda: -1)
point_zero_dict = defaultdict(lambda: (0,0))
message_dict = defaultdict(lambda: 'No Message')
def print_all(d):
    for item in d:
        print(item)
print_all(minus_one_dict)
print_all(point_zero_dict)
print_all(message_dict)
print()