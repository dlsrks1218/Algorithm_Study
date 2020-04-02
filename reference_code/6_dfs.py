def bfs(graph, start_node):
    visit = []
    queue = []

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit


def dfs(graph, start_node):
    visit = []
    stack = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit


def test(graph, start_node):
    print(bfs(graph,start_node))
    print(dfs(graph,start_node))


if __name__ == '__main__':
    graph  = {
        'A': ['B'], 
        'B': ['A', 'C', 'H'], 
        'C': ['D'], 
        'D': ['C', 'E', 'G'], 
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

    test(graph, 'A')