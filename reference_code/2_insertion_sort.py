# 삽입 정렬 / 시간 복잡도 : O(N)
# 두번째 자료부터 시작하여 앞 자료와 비교하여 자리 바꾸고 정렬된 배열과 
# 자료 갯수 만큼 비교 시 정렬 완료

# 주어진 데이터를 Insertion Sort를 사용하여 정렬 하시오. 데이터의 최대 크기는 100이다.

# 1 // 전체 test case 수
# 5 // 데이터 크기
# 1 4 5 2 3

def insertion_sort(data, size):
    for i in range(1, size):
        key = data[i]
        j = i-1
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j-=1
        data[j+1] = key

    return data
            
T = int(input())

for i in range(T):
    size = int(input())
    data = list(map(int, input().split()))
    # print(data, size)
    
    insertion_sort(data, size)

    print('#%d' %(i+1), end='')
    for idx, datum in enumerate(data):
        if idx < len(data):
            print(' %d' %(datum), end='')
