from sys import stdin

# input
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

def dfs(cur_node, row, foot_prints):
    foot_prints += [cur_node]
    for search_node in range(len(row[cur_node])):
        if row[cur_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints

def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        cur_node = queue.pop(0)
        for search_node in range(len(matrix[cur_node])):
            if matrix[cur_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints

n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]

print('\n\ninitiate adjacency matrix')
for line in matrix:
    print(line)

for _ in range(m):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1
    
print('make adjacency matrix')
for line in matrix:
    print(line)

print('\ndfs result :', *dfs(v, matrix, []))
print('bfs result :', *bfs(v))