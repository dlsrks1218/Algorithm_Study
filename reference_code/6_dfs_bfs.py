from collections import deque

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


def test(graph, start_node):
    print(BFS(graph,start_node))
    print(DFS(graph,start_node))


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