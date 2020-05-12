def rotate(matrix, d):
    N = len(matrix)
    new_matrix = [[0] * N for i in range(N)]

    if d % 4 == 1:
        for i in range(N):
            for j in range(N):
                new_matrix[j][N - 1 - i] = matrix[i][j]
    elif d % 4 == 2:
        for i in range(N):
            for j in range(N):
                new_matrix[N - 1 - j][N - 1 - i] = matrix[j][i]
    elif d % 4 == 3:
        for i in range(N):
            for j in range(N):
                new_matrix[N - 1 - j][i] = matrix[i][j]
    else:
        new_matrix = matrix

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()
    
    print()

    for i in range(N):
        for j in range(N):
            print(new_matrix[i][j], end=' ')
        print()
    
    return new_matrix

def solution(key, lock):
    ans = 0
    options = [0, 1, 2, 3]

    # for i in range(4):
    #     print('-', i, '-')
    #     rotate(key, i)
    #     print('-----\n')

    

    return ans


def test(key, lock, ans):
    try:
        assert len(key) >= 3 and len(key) <= 20
        assert len(lock) >= 3 and len(lock) <= 20
        assert(solution(key, lock) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]], True)