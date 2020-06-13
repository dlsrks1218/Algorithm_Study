def ms1(lst):
    # 매번 병합 결과를 담을 배열을 새로 생성하기 때문에 비효율적임
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = ms1(lst[:mid])
    right = ms1(lst[mid:])
    l_idx, r_idx = 0, 0
    merged_lst = []

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            merged_lst.append(left[l_idx])
            l_idx += 1
        else:
            merged_lst.append(right[r_idx])
            r_idx += 1

    merged_lst += left[l_idx:]
    merged_lst += right[r_idx:]

    return merged_lst

def ms2(lst):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l_idx, h_idx = low, mid

        while l_idx < mid and h_idx < high:
            if lst[l_idx] < lst[h_idx]:
                temp.append(lst[l_idx])
                l_idx += 1
            else:
                temp.append(lst[h_idx])
                h_idx += 1
        
        while l_idx < mid:
            temp.append(lst[l_idx])
            l_idx += 1

        while h_idx < high:
            temp.append(lst[h_idx])
            h_idx += 1

        for i in range(low, high):
            lst[i] = temp[i - low]
        
    return sort(0, len(lst))

def ms3(lst, low, high):
    def merge(low, mid, high):
        temp = []
        l_idx, h_idx = low, mid

        while l_idx < mid and h_idx < high:
            if lst[l_idx] < lst[h_idx]:
                temp.append(lst[l_idx])
                l_idx += 1
            else:
                temp.append(lst[h_idx])
                h_idx += 1
            
        while l_idx < mid:
            temp.append(lst[l_idx])
            l_idx += 1
        while h_idx < high:
            temp.append(lst[h_idx])
            h_idx += 1
        
        for i in range(low, high):
            lst[i] = temp[i - low]

    if high - low < 2:
        return
    mid = (low + high) // 2
    ms3(lst, low, mid)
    ms3(lst, mid, high)
    merge(low, mid, high)

    return lst


lst = [9,8,7,6,5,4,3,2,1]
# print(ms1(lst))

# ms2(lst)
# print(lst)

print(ms3(lst, 0, len(lst)))