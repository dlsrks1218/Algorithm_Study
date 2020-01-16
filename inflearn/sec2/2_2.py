# # ascii코드 상 알파벳 대문자는 65~90 / 알파벳 소문자는 97~122
# # 문자를 아스키코드로 변환하는 함수 -> ord(문자)
# # 아스키코드를 문자로 변환하는 함수 -> chr(숫자)

# def isAlpha(ch):
#     if (ord(ch) >=64 and ord(ch) <= 90) or (ord(ch) >=97 and ord(ch) <= 122):
#         return True
#     else:
#         return False

# inp = input()
# inp1 = ''
# for ch in inp:
#     if isAlpha(ch) == False:
#         inp1 += ch

# num = int(inp1)
# print(num)

# ans = [1]

# for i in range(2, num+1):
#     if num%i == 0:
#         ans.append(i)

# print(len(ans))

# inp = 'g0en2Ts8eSoft'
inp = input()
res = 0
for x in inp:
    if x.isdecimal():
        res = res*10+int(x)
print(res)

cnt = 0

for i in range(1, res+1):
    if res%i == 0:
        cnt+=1

print(cnt)






