def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
    return li

li = [1,6,1,8,6,4,3,7,9,3,1,4,3]
print(select_sort(li))