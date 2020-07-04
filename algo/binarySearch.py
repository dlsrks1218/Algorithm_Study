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
    """타겟 숫자의 인덱스 찾기

    Args:
        arr (int): [description]
        targetNum (int): [description]

    Returns:
        idx: [description]
    """
    
    start, end = 0, len(arr) - 1
    while start <= end:
        midIndex = (start + end) // 2
        if arr[midIndex] == targetNum:
            return midIndex
        elif arr[midIndex] < targetNum:
            start = midIndex + 1
        elif arr[midIndex] > targetNum:
            end = midIndex - 1
	# print('arr[', midIndex, '] =', arr[midIndex])
    # print(arr[midIndex])
        # print(start, end)
    return -1


arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
target = 8
target_idx = bs(arr, target)
print('target num :', target)
print('target_index :', target_idx)
