def insert_sort_gap(li, gap):         # 传入列表和gap也就是d
    for i in range(gap, len(li)):     # 抓牌指针从gap（索引）开始一直循环到最后一个元素
        tmp = li[i]                   # 记录抓上来的牌
        j = i - gap                   # j对应的是j-gap
        while j >= 0 and li[j] > tmp: # 当手牌指针指向了一个数，且此时的数大于抓的牌
            li[j + gap] = li[j]       # j指向的手牌在这组往后挪一个单位
            j -= gap                  # j指针往前挪一个单位
        else: 
            li[j + gap] = tmp         # 如果j越下界（j=-gap）或者手牌值小于抓牌值，那么就将抓的牌插入到j指针后面

def shell_sort(li):
    n = len(li)
    d = n // 2 
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2

li = list(range(100))
import random
random.shuffle(li)
shell_sort(li)
print(li)