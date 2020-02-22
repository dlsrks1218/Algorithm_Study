def dfs(graph, start_node):
    visit = dict()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(graph[node])
    
    return list(visit.keys())


def bfs(graph, start_node):
    visit = dict()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit[node] = True
            queue.extend(graph[node])

    return list(visit.keys())

    
graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D', 'G'],
        'D': ['C', 'E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
}

print('dfs 결과 :',dfs(graph, 'A'))
print('bfs 결과 :',bfs(graph, 'A'))

# # T = test case 갯수
# T = int(input())
# # v = vertex 갯수
# v, start = map(int, input().split())

# vertex = 0
# m = [[0,0] for i in range(v)]
# visit = [0 for i in range(v)]

# print(m, visit)

# def dfs(v):
#     visit[v] = 1
#     for i in range(1, vertex):
#         if m[v][i] == 1 and not visit[i]:
#             print(i)
#             dfs(i)

# for i in range(T):
#     graph = dict()
#     v1, v2 = 0, 0
#     while True:
#         v1, v2 = map(int, input().split())
#         if v1 == -1 and v2 == -1:
#             break
#         graph[v1] = graph.get(v1, []) + [v2]
#         # m[v1][v2] = 1
#         # m[v2][v1] = 1
    
#     print('#%d %d ' %(T, start))
#     dfs(graph, start)
#     print('\n')

