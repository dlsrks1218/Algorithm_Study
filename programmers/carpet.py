import math

def factor_pair_lst(lattice):
    pair_lst = []
    tmp = []
    for i in range(1, lattice+1):
        tmp = [0, 0]
        if lattice % i == 0:
            tmp[0], tmp[1] = i, lattice // i
            if tmp[0] >= tmp[1]:
                pair_lst.append(tmp)
    return pair_lst


def solution(brown, red):
    answer = []
    lattice = brown + red

    pair_lst = factor_pair_lst(lattice)

    red_lst = factor_pair_lst(red)

    for pair in pair_lst:
        for red in red_lst:
            if pair[0] > red[0]+1 and pair[1] > red[1]+1 and lattice > (red[0]+1)*(red[1]+1):
                answer = pair
    # print(answer)
    return answer


def test(brown, red, ans):
    try:
        assert brown >= 8 and brown <= 5000
        assert red >= 1 and red <= 2000000
        assert(solution(brown, red) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')

    
if __name__ == '__main__':
    test(10, 2, [4,3])
    test(8, 1, [3,3])
    test(24, 24, [8,6])
    # test(brown, red, ans)