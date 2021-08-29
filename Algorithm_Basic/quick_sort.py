def quick_sort(li,left,right): #li:待处理列表，left：待处理区域的左索引，right：待处理区域的右索引
    if left < right:             #在左索引<右索引的时候运行（即待处理区域小于两个数不需要处理）
        mid = partition(li, left, right) #partition：将li列表的待处理区域进行归类，返回p元素索引值
        quick_sort(li, left, mid - 1)    #递归的方式处理p元素左边的区域
        quick_sort(li, mid + 1, right)   #递归的方式处理p元素右边的区域

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left