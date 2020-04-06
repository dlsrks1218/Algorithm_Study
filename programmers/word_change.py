from collections import defaultdict, deque

transistable = lambda a,b: sum((1 if x!=y else 0) for x,y in zip(a,b)) == 1

def solution(begin, target, words):
    graph = defaultdict(list)
    graph[begin] = set(filter(lambda x: transistable(begin, x), words))
    for word in words:
        graph[word] = set(filter(lambda x: transistable(word, x), words))
    # print(graph)

    q = deque([(begin, 0)])

    if target not in words:
        return 0
        
    while q:
        node, level = q.popleft()
        for word in graph[node]:
            if word == target:
                return level+1
            else:
                q.append((word, level+1))
    return 0

# def solution(begin, target, words):
#     def wordcmp(w1, w2):
#         cnt = 0
#         for ch in w1:
#             if ch in w2:
#                 cnt += 1
#         if cnt < len(w1)-1:
#             return 0
#         elif cnt == len(w1)-1:
#             return 1
    
#     ans = 0
#     visited = OrderedDict()
#     cursor = begin

#     if target not in words:
#         print(ans)
#         return ans
    
#     for word in words:
#         if len(visited) == len(words) or cursor == target:
#             print(ans, visited)
#             break
#         if wordcmp(cursor, word) == 1:
#             visited[word] = True
#             cursor = word
#             ans += 1
#             print(cursor)
#     return ans


def test(begin, target, words, ans):
    try:
        assert begin != target
        assert len(words) >= 3 and len(words) <= 50
        assert [word for word in words if len(word)>=3 and len(word)<=10]
        assert(solution(begin, target, words) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], 4)
    test("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0)
    test('hit', 'hhh', ['hhh', 'hot', 'hht'], 2)