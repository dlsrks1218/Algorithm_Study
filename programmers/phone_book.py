def solution(phone_book):
    for p in phone_book:
        for pp in phone_book:
            if p != pp:
                if len(p) < len(pp) and p == pp[:len(p)]:
                    return False
                else:
                    pass
    return True


print(solution(['119', '97674223', '1195524421']))
print(solution(['123', '456', '789']))
print(solution(['12','123','1235','567','88']))
print(solution(['119', '1192456']))
print(solution(['1192456', '119']))