from itertools import permutations

def check(banned_id, candidate_users):
    for ban, can in zip(banned_id, candidate_users):
        # print(ban, can)

        if len(ban) != len(can):
            return False
        for b, c in zip(ban, can):
            if b == '*':
                continue
            elif b != c:
                return False
    return True


def solution(user_id, banned_id):
    ans = []

    for candidate_users in permutations(user_id, len(banned_id)):
        if check(banned_id, candidate_users) is True:
            candidate_users = set(candidate_users)
            if candidate_users not in ans:
                ans.append(candidate_users)
            
    # for item in ans:
    #     print(item)

    return len(ans)



def test(user_id, banned_id, ans):
    try:
        assert len(user_id) >= 1 and len(user_id) <= 8
        assert len(banned_id) >= 1 and len(banned_id) <= len(user_id)
        assert list(filter(lambda x: len(x)>=1 and len(x)<=8, banned_id))
        assert(solution(user_id, banned_id) == ans)
        print('정답입니다 :)')
    except AssertionError as err:
        print('틀렸습니다 :(')


if __name__ == '__main__':
    test(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"], 2)
    test(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"], 2)