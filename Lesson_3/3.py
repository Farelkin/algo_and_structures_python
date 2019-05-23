# 3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

list1 = [random.randint(1, 10) for i in range(10)]

print(list1)
max = list1[0]
min = list1[0]

for i in range(len(list1)):
    if max < list1[i] or max == list1[i]:
        max = list1[i]
        max_index = i
    elif min > list1[i] or min == list1[i]:
        min = list1[i]
        min_index = i

list1[max_index] = min
list1[min_index] = max

print(list1)