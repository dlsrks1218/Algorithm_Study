def solution(inp1, inp2):
    ans = 0

    visited = [0 for i in range(inp1)]
    def dfs(inp2, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(inp2)):
                if inp2[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] == 0:
            dfs(inp2, visited, i)
            ans+=1
        i+=1
    
    # print(ans)

    return ans


def test(inp1, inp2, ans):
    try:
        assert inp1 >= 1 and inp1 <= 200
        assert(solution(inp1, inp2) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    # test(3, [[1,1,0], [1,1,0], [0,0,1]], 2)
    test(3, [[1,1,0], [1,1,1], [0,1,1]], 1)