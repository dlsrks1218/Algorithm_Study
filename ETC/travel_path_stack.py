tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]

def solution(tickets):
    graph = dict()
    for s, e in tickets:
        graph[s] = graph.get(s, []) + [e]
    print(graph)

    for key in graph.keys():
        graph[key].sort(reverse=True)
    print(graph)

    stack = ['ICN']
    path = []

    while stack:
        top = stack[-1]
        
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(graph[top][-1])
            graph[top] = graph[top][:-1]

    print(path)
    path.reverse()
    return path

solution(tickets)
