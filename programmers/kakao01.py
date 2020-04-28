def solution(board, moves):
    ans = 0

    bucket = []

    for line in board:
        print(line)

    # for j in range(len(board[0])):
    #     for i in range(len(board[0])):
    #         print(board[i][j], end=' ')
    #     print()

    for i in range(len(board[0])):
        for j in range(len(board[0])):
            print(board[j][i], end=' ')
        print()

    moves = [m-1 for m in moves]
    print(moves)

    for m in moves:
        for i in range(len(board[0]) - 1):
            if bucket[0] == board[i+1][m]:
                bucket.pop()
                ans += 1
            if board[i][m] != 0:
                bucket.append(board[i][m])
                board[i][m] = 0
        print()

    # for m in moves:
    #     for i in range(len(board[0]) - 1):
    #         if bucket[0] == board[i][m]:
    #             bucket.pop()
    #             ans += 1
    #         if i != 0:
    #             bucket.push(board[i][m])
    #             board[i][m] = 0
    return ans


def test(board, moves, answer):
    try:
        assert len(board) >= 5 and len(board) <= 30
        # assert min(board) >= 0 and max(board) <= 100
        assert len(moves) >= 1 and len(moves) <= 1000
        assert min(moves) >= 1 and max(moves) <= len(board[0])
        assert(solution(board, moves) == answer)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4], 4)