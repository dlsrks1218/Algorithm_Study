"""
이진탐색
* 탐색 범위를 줄여나가며 찾는다

장점
* 빠르고 실제로 사용됨
* O(log n)

단점
* 정렬이 되어있어야 함, 구현이 어려움

핵심 로직
* 중간 인덱스 값을 구한다
"""


def bs(arr, targetNum):
    start, end = 0, len(arr) - 1
    midIndex = len(arr) // 2
    indexValue = arr[midIndex]
    # 종료 조건
    if indexValue == targetNum:
        return midIndex
    elif indexValue < targetNum:
        start = midIndex + 1
    elif indexValue > targetNum:
        end = midIndex - 1
	# print('arr[', midIndex, '] =', indexValue)
    print(indexValue)
    # return -1


arr = [1, 2, 3, 4, 5, 6, 7]
bs(arr, 6)
