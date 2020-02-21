# 다익스트라 : 하나의 정점으로부터 다른 모든 정점까지의 최단 경로를 구하는 알고리즘

def solution(n, edge):
    
    dist = [999999 for x in range(n+1)]
    prev = [-1 for x in range(n+1)]
    Q = set(); # 아직 미방문상태인 정점들을 넣는 집합
    
    for i in range(1, n+1):
        Q.add(i); # 모든 정점들을 집합 Q에 넣는다
        
    dist[1] = 0; # 1번 노드부터 시작하므로, 1번 노드와의 거리는 0으로 초기화
    
    while len(Q) > 0: # 집합 Q가 빌 때까지...
        mindist = 99999
        u = -1
        for i in range(1, n+1): # 미방문 정점들 중 출발점으로부터의 거리가 가장 짧은 정점 찾기
            if i not in Q:
                continue
            if dist[i] < mindist:
                mindist = dist[i]
                u = i
                
        Q.remove(u); # 그 정점을 방문하고 Q에서 지운다
        
        neighbor = []
        for e in edge: # 정점 u의 이웃들을 찾는다
            if e[0] == u:
                neighbor.append(e[1])
            elif e[1] == u:
                neighbor.append(e[0])
        
        for nei in neighbor: # 정점 u의 이웃들을 하나씩 보면서
            alt = dist[u] + 1; # 다음 정점까지의 거리 = 지금까지의 거리 + 1
            if alt < dist[nei]: # 이게 기존 값보다 더 작으면 갱신
                dist[nei] = alt
                prev[nei] = u
    
    del dist[0]; # 편의상 0번 정점에는 999999를 저장해놨으므로...
    max_dist = max(dist)
    answer = dist.count(max_dist)
    
    print(answer)
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)



