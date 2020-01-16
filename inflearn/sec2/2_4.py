n = int(input())
n_lst = list(map(int, input().split()))

m = int(input())
m_lst = list(map(int, input().split()))

result = n_lst+m_lst


def ascending_order_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst

print(result)
print(ascending_order_sort(result))

