def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                exchange = True
                li[j], li[j+1] = li[j+1], li[j]
        if not exchange:
            return li
    return li

list1 = [1,7,6,3,7,1,6,9]
print(bubble_sort(list1))