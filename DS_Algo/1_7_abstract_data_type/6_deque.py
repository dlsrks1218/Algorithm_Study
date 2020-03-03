from collections import deque

q = deque(['buffy', 'jender', 'willo'])
print(q)

# q.append('jiles')
# print(q)

# q.popleft()
# print(q)

# q.pop()
# print(q)

# q.appendleft('angel')
# print(q)

# q.append('demon')
# print(q)

q.rotate(3)
print(q)

q.rotate(-1)
print(q)