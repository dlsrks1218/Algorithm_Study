from itertools import permutations

def solution(expression):
    answer = 0

    operator = ['+', '-', '*']
    num_lst = []
    oper_lst, oper_idx_lst = [], []
    tmp_idx = 0

    for idx, ch in enumerate(expression):
        if ch in operator:
            oper_idx_lst.append(idx)
            oper_lst.append(ch)
            num_lst.append(expression[tmp_idx:idx])
            tmp_idx = idx + 1

    candidates = list(permutations(set(oper_lst), len(set(oper_lst))))
    print(candidates)

    for cand in candidates:
        for idx, ch in enumerate(expression):
            if ch == cand[0]:
                


    print(num_lst)
    return answer

solution("100-200*300-500+20")
# solution("100-200*300-500+20", 60420)