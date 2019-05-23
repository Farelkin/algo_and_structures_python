# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random

lst1 = random.sample(range(-10, 10), 1)

index_min = 0

max_min = 0

for index, val in enumerate(lst1):

    if val < max_min:
        max_min = val

        index_min = index

print(lst1)

print(f'Максимальный отрицательный элемент в массиве {max_min} на позиции {index_min}')