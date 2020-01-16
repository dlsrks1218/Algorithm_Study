arr = []
visited = []

def dfs(length = 0):
    if length == m:
        for i in range(m):
            print(arr[i])
        print()
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr[length] = i
        dfs(length+1)
        visited[i] = False

n, m = map(int, input().split())

for i in range(1, n):
    visited[i] = True
    arr[0] = i
    dfs(1)
    visited[i] = False

    