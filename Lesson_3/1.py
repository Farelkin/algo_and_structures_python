# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list1 = [x for x in range(2, 100)]
list2 = {x: 0 for x in range(2, 10)}
count = 0

for i in list2.keys():
    for j in list1:
        if j % i == 0:
            list2[i] += 1
            count += 1

for i in list2.keys():
    print(f'Числу {i} в диапазоне от 2 до 99 кратно {list2[i]} чисел.')
print(f'Всего {count} кратных чисел')
