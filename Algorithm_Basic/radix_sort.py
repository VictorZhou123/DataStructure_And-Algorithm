def radix_sort(li):
    # 找出li中最大的数
    max_num = max(li)
    # 根据最大值的位数进行相应次数的循环
    it = 0
    while 10**it <= max_num:
        # 创造0-9的新桶子
        buckets = [[] for _ in range(10)]
        for var in li:
            # 计算出var要去哪个桶
            digit = (var % (10 ** (it + 1))) // 10 ** it
            buckets[digit].append(var)
        # 将排列好的数装回li列表
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1
    

import random
li = [random.randint(0,1000) for _ in range(1000)]
radix_sort(li)
print(li)