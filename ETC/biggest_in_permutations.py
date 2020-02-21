from itertools import permutations

# numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]

ans_set = set()

for item in list(permutations(numbers)):
    tmp = ''
    for n in item:
        tmp+=str(n)
    ans_set.add(int(tmp))

print(max(ans_set))