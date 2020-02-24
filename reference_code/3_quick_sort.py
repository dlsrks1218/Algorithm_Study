# 퀵 정렬
# 퀵 정렬은 기준키(pivot)를 기준으로 작거나 같은 값을 지닌 데이터는 앞으로, 
# 큰 값을 지닌 데이터는 뒤로 가도록 하여 작은 값을 갖는 데이터와 큰 값을 갖는 데이터로 분리해가며 정렬하는 방법이다.

# 주어진 데이터를 Quick Sort를 사용하여 정렬 하시오. 데이터의 최대 크기는 100이다.

# 1 // 전체 Test case 수
# 5 // 데이터 크기
# 1 4 5 2 3

def quick_sort(first, last):
    tmp = 0

    if first < last:
        pivot = first
        i = first
        j = last
        while i < j:
            while data[i] <= data[pivot] and i < last:
                i+=1
            while data[j] > data[pivot]:
                j-=1
            if i < j:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp

        tmp = data[pivot]
        data[pivot] = data[j]
        data[j] = tmp
 
        quick_sort(first, j - 1)
        quick_sort(j + 1, last)

    return data

T = int(input())

for i in range(T):
    size = int(input())
    data = list(map(int, input().split()))
    # print(data, size)

    quick_sort(0, size-1)

    print('#%d' %(i+1), end='')
    for idx, datum in enumerate(data):
        if idx < len(data):
            print(' %d' %(datum), end='')

