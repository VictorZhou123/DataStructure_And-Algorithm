def sift(li, low, high): #high:堆的最后一个元素位置，low：堆顶位置
    i = low
    j = 2 * i + 1
    tmp = li[i]

    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def heap_construction(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        # i表示建堆的时候调整部分的根的下标
        sift(li, i, n-1)
        #建堆完成


def heap_sort(li):
    heap_construction(li)
    n = len(li)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)

# li = [1,7,6,4,5,3,4,6,9,8]
# heap_sort(li)
# print(li)

def topk(li, k):
    #构造小根堆
    heap = li[0:k]
    heap_construction(heap)
    #遍历余下各数替换掉堆顶的最小数然后再向下调整
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    #堆排序
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap

import random
li = list(range(100))
random.shuffle(li)

k = 10
heap = topk(li, k)
print(heap)