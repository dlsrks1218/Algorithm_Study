def dfs(graph, N, key, footprint):
    # print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret

def solution(tickets):
    answer = []

    graph = dict()

    N = len(tickets)

    for s, e in tickets:
        graph[s] = graph.get(s, []) + [e]
        graph[s].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])
    print(answer)
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

solution(tickets)