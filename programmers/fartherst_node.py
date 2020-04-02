from collections import defaultdict

def solution(inp1, inp2):
    def DFS(graph, start_node):
        visited = []
        # stack = []
        # stack.append(start_node)
        stack = [start_node]
        while stack:
            print(stack)
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(graph[node])
        return visited

    def BFS(graph, start_node):
        visited = []
        queue = [start_node]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(graph[node])
            print(queue)
        return visited
    
    ans = 0

    g = defaultdict(list)

    for v in inp2:
        g[v[0]].append(v[1])
        g[v[1]].append(v[0])

    print(g)
    print(DFS(g, 1))
    # print(BFS(g, 1))

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