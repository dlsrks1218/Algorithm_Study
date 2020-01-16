n = int(input())

# def palindrome(word):
#     answer = True
#     mid = len(word)//2
#     for i in range(mid):
#         if word[mid-i] != word[mid+i]:
#             answer = False
#         else:
#             answer = True
#     return answer
# 
# word_lst = []
# for i in range(n):
#     inp = input()
#     word_lst.append(inp.upper())

# for idx, word in  enumerate(word_lst):
#     if palindrome(word) == True:
#         print('#%d YES' %(idx+1))
#     else:
#         print('#%d NO' %(idx+1))

for i in range(n):
    s = input()
    s = s.upper()
    ## s[::-1] 는 s를 reverse한 문자열
    if s == s[::-1]:
        print('#%d YES' %(i+1))
    else:
        print('$%d NO' %(i+1))


