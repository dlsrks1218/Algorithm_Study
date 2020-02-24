# 재귀
# 재귀는 수학이나 컴퓨터 과학 등에서 자신을 정의할 때 자기 자신을 재참조하는 방법을 뜻한다. 
# 주로 이 방법은 함수에 적용한 재귀 함수(Recursion Function)의 형태로 많이 사용된다.

# 주어진 수의 Factorial 값을 구해 아래와 같이 출력하시오. 주어지는 수는 1 이상 20 이하의 수이다.

# 3 // 전체 Test case 수
# 9 // Test case index
# 12
# 20

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

T = int(input())

for i in range(T):
    num = int(input())
    print('#%d %d! = %d' %(i+1, num, factorial(num)))