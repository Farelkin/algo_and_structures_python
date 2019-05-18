"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random

lim_min_int = int(input('lim_min_int = '))
lim_max_int = int(input('lim_max_int = '))

print(int(random.random() * (lim_max_int - lim_min_int + 1) + lim_min_int))

lim_min_float = int(input('lim_min_float = '))
lim_max_float = int(input('lim_max_float = '))

print(random.random() * (lim_max_float - lim_min_float + 1) + lim_min_float)

print('---------------only small char!---------------')
lim_min_chr = ord(input('lim_min_chr = '))
lim_max_chr = ord(input('lim_max_chr = '))

print(chr(int(random.random() * (lim_min_chr - lim_max_chr + 1) + lim_max_chr)))

