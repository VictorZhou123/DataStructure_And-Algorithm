def insertion_sort(li):
    for i in range(1,len(li)):
        temp = li[i]                #拿temp存好摸的牌的值
        j = i-1                     #j是手里牌(有序区)一个从后往前的指针
        while j>=0 and li[j]>temp:  #当指针不为负数（为负数时指针无效了），且指针指向的牌大于抓的牌时
            li[j+1] = li[j]         #指针指向的牌向后移动一位
            j -= 1                  #同时指针向前移动一位
        else:
            li[j+1] = temp          #while循环条件不满足时，将牌插在比较的牌(指针)的后面。
        print(li)
    return li

li = [1,6,1,8,6,4,3,7,9,3,1,4,3]
print(li)
insertion_sort(li)
