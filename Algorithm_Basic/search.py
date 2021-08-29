def linear_search(li, val):
    for ind,v in enumerate(li):
        if v == val:
            return ind
        else:
            return None

def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:        #候选区有值
        mid = (left+right) // 2
        if li[mid] == val:      #mid的值等于val
            return mid
        elif li[mid] > val:     #待查找的值在mid左侧
            right = mid - 1
        else:                   #待查找的值在mid右侧
            left = mid + 1
    else:
        return None

