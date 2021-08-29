def bucket_sort(li, n = 100, max_num = 1000):
    # 创建0~99的空桶
    buckets = [[] for _ in range(n)]
    for var in li:
        # 计算出var需要去哪个桶，计算结果如果超过了99则直接分配到第99桶内
        index = min((var // ((max_num // n) - 1)), n - 1)
        buckets[index].append(var)
        # 给新加入的数进行冒泡
        for i in range(len(buckets[index]) - 1, 0, -1):
            if buckets[index][i - 1] > buckets[index][i]:
                buckets[index][i], buckets[index][i - 1] = buckets[index][i - 1], buckets[index][i]
            else:
                break
    li.clear()
    # 按顺序挨个加入到li中
    for buc in buckets:
        li.extend(buc)

import random
li = [random.randint(0, 1000) for _ in range(1000)]
bucket_sort(li)
print(li)