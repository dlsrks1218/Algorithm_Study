import random

n = int(input())

money_lst = []

for i in range(n):
    money = 0
    tmp = input().split()
    tmp.sort()
    a,b,c = map(int, tmp)
    if a==b and b==c:
        money = 10000+a*1000
    elif a==b:
        money = 1000+a*100
    else:
        money = a*100

    # print(money)
    money_lst.append(money)

print(max(money_lst))


# 3
# 3 3 6
# 2 2 2
# 6 2 5
# class Person:
#     def __init__(self):
#         self.choice_lst = []
#         self.prize = 0

#     def roll(self):
#         for dice in dice_lst:
#             self.choice_lst.append(random.choice(dice))

#         for choice in self.choice_lst:
#             tmp = choice
#             if self.choice_lst.count(tmp) == 1:
#                 self.prize = max(self.choice_lst)*100
#             elif self.choice_lst.count(tmp) == 2:
#                 self.prize = 1000 + tmp * 100
#             elif self.choice_lst.count(tmp) == 3:
#                 self.prize = 10000 + (tmp*1000)

#         # print(self)
#         # print(self.choice_lst)
#         # print(self.prize)

#     def getPrize(self):
#         return self.prize

#     def getChoiceLst(self):
#         return self.choice_lst 

# n = int(input())

# dice_lst = []

# for i in range(3):
#     dice = [i for i in range(1, 7)]
#     dice_lst.append(dice)

# person_lst = []

# for i in range(n):
#     pName = 'person'
#     pName+=str(i+1)
#     pName = Person()
#     person_lst.append(pName)

# prize_lst = []

# for person in person_lst:
#     person.roll()
#     prize_lst.append(person.getPrize())

# print(max(prize_lst))
