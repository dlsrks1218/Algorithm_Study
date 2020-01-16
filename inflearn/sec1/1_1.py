# k번쨰 약수 구하기
import sys

# sys.stdin = open('/Users/jonghyunlim/Documents/Project/Algorithm/inflearn/AA/1_1_input.txt', 'rt')
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i == 0:    #약수
        cnt+=1
    if cnt == k:    #k번째 약수 발견
        print(i)
        break
else:   # for문을 모두 돌아 for문 내 break가 작동하지 않았을 때
    print(-1)

