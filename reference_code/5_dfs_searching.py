# 깊이 우선 탐색은 맹목적 탐색방법의 하나로 한 노드를 시작으로 
# 인접한 다른 노드를 재귀적으로 탐색해가고 끝까지 탐색하면 다시 위로 와서 다음을 탐색하여 검색한다.

# 숫자가 있는 원은 정점(Vertex)라고 하고, 정점과 정점을 잇는 연결선을 간선(Edge)이라고 한다. 정점의 최대 개수는 30개이다.
# 정점과 정점의 연결관계가 인접행렬로 주어졌을 때, DFS를 이용하여 시작 정점으로부터 모든 정점을 탐색한 결과를 순서대로 화면에 출력하시오.

# 1 //test case 개수
# 8 1 // 정점의 개수, 시작 정점
# 1 2 // 정점 간 연결 관계. 1과 2가 연결
# 1 3
# 2 4
# 2 5
# 4 8
# 5 8
# 3 6
# 3 7
# 6 8
# 7 8
# -1 -1 // 입력 끝

def dfs(start_node, m, visit, vertex):
    visit[start_node] = 1
    for i in range(1, vertex+1):
        if m[start_node][i] == 1 and not visit[i]:
            print(' %d' %(i), end='')
            dfs(i, m, visit, vertex)


T = int(input())

for i in range(T):
    vertex, start = map(int, input().split())
    
    m = [[0] * (vertex+1) for i in range(vertex+1)]
    visit = [0 for i in range(vertex+1)]

    while True:
        v1, v2 = map(int, input().split())
        if v1 == -1 and v2 == -1:
            break
        m[v1][v2] = m[v2][v1] = 1
    
    print('#%d %d' %(i+1, start), end='')
    dfs(start, m, visit, vertex)
