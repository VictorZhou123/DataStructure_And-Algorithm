def count_sort(li, maxcount=100):
    count = [0 for _ in range(maxcount+1)]
    for var in li:
        count[var] += 1
    li.clear()
    for index, var in enumerate(count):
        for i in range(var):
            li.append(index)

import random
li = list(range(100))
random.shuffle(li)
count_sort(li)
print(li)