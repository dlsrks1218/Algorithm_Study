def solution(board, moves):
    ans = 0
    bucket = []
    moves = [m-1 for m in moves]

    # for i in range(len(board)):
    #     print('moves : ', i , end=' -> ')
    #     for j in range(len(board)):
    #         print(board[j][i], end=' ')
    #     print()

    for m in moves:
        for i in range(len(board)):
            tmp = board[i][m]
            if tmp != 0:
                if len(bucket) > 0 and bucket[-1] == tmp:
                    ans += 2
                    bucket.pop()
                else:
                    bucket.append(tmp)
                board[i][m] = 0
                break

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