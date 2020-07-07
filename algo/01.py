def solution(name_list):
    for idx, name in enumerate(name_list):
        # print(idx, name)
        for name1 in name_list[idx+1:]:
            if name == name1 or name in name1:
                return True

    return False

def test(name_list):
    try:
        assert len(name_list) >= 0 and len(name_list) <= 10000
        for name in name_list:
            assert len(name) >= 1 and len(name) <= 16
        print(solution(name_list))
    except AssertionError as err:
        print('값을 다시 입력해주세요')

if __name__ == '__main__':
    test(["가을", "우주", "너굴"])
    test(["봄", "여울", "봄봄"])
    test(["너굴", "너울", "여울", "서울"])
    test(["가나다", "가나다라"])
    test(["가나다", "가다나라"])