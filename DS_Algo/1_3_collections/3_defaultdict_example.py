from collections import defaultdict

def defaultdict_example():
    pairs = {('a', 1), ('b', 2), ('c', 3)}

    # 일반 딕셔너리
    d1 = {}

    for k, v in pairs:
        if k not in d1:
            d1[k] = []
        d1[k].append(v)
    print(d1)

    # defaultdict
    d2 = defaultdict(list)
    for k, v in pairs:
        d2[k].append(v)
    print(d2)


if __name__ == '__main__':
    defaultdict_example()