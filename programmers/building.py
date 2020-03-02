def solution(heights):
    ans = [0 for _ in range(len(heights))]
    for i in range(len(heights)-1, -1, -1):
        tmp = heights.pop()
        for j in range(len(heights)-1, -1, -1):
            if tmp < heights[j]:
                ans[i] = j+1
                break
    # while heights:
    #     tmp = heights.pop()
    #     for i in range(len(heights)-1, -1, -1):
    #         if tmp < heights[i]:
    #             ans[len(heights)] = i+1
    #             break
    return ans

print(solution([6,9,5,7,4]))