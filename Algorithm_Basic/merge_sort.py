def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmpli = []
    while i<=mid and j<=high:      # 当i,j指针都能取到数
        if li[i] <= li[j]:         # 比较两指针的数，比较小的放到新列表中
            tmpli.append(li[i])
            i += 1
        else:
            tmpli.append(li[j])
            j += 1

    # 上面的while循环截止时必有一指针已经越界
    while i <= mid:                #判断两种情况
        tmpli.append(li[i])
        i += 1
    while j <= high:
        tmpli.append(li[j])
        j += 1
    li[low:high+1] = tmpli

# li = [10,8,6,4,2,9,7,5,3,1]
# merge(li, 0, 4, len(li)-1)
# print(li)

def merge_sort(li, low, high):           # 对列表li在low到high范围进行一次归并排序（无需考虑列表是不是两段有序）
    if low < high:
        mid = (low + high)//2
        merge_sort(li, low, mid)         # 在mid左右进行归并排序，确保两边都是有序的。给merge函数创造条件
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)        # 对整个li列表进行归并


import random
li = list(range(1000))
print(li)
random.shuffle(li)
merge_sort(li, 0, len(li)-1)
print(li)
