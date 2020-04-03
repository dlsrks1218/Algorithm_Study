from collections import defaultdict, deque

def solution(inp1, inp2):
    def DFS(graph, start_node):
        visited = {}
        stack = [start_node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited[node] = True
                stack.extend(graph[node])
        return list(visited.keys())

    def BFS(graph, start_node):
        visited = {}
        q = deque()
        q.append(start_node)
        while q:
            node = q.popleft()
            if node not in visited:
                visited[node] = True
                q.extend(graph[node])
        return list(visited.keys())
    
    ans = 0

    g = defaultdict(list)

    for v in inp2:
        g[v[0]].append(v[1])
        g[v[1]].append(v[0])

    print(g)
    print(DFS(g, 1))
    print(BFS(g, 1))

    return ans


def test(inp1, inp2, ans):
    try:
        assert inp1 >= 2 and inp1 <= 10000
        assert len(inp2) >= 1 and len(inp2) <= 50000
        assert(solution(inp1, inp2) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test(6, [[3,6], [4,3], [3,2], [1,3], [1,2], [2,4], [5,2]], 3)