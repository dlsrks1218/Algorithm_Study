from itertools import permutations
from itertools import combinations

def isPrime(num):
    if num<2:
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True

def list_to_num(lst):
    s = ''
    for item in lst:
        s+=str(item)
    return int(s)

numbers = input()
num_list = []

for ch in numbers:
    num_list.append(ch)

all_case = set()
for i in range(len(num_list)):
    tmp = set(permutations(num_list, i+1))
    for t in tmp:
        if isPrime(list_to_num(list(t))):
            all_case.add(list_to_num(list(t)))
print(len(all_case))