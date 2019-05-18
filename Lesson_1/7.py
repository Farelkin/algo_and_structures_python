"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

len_1 = float(input('len_1 = '))
len_2 = float(input('len_2 = '))
len_3 = float(input('len_3 = '))

if (len_1 + len_2 <= len_3) or (
        len_1 + len_3 <= len_2) or (
        len_2 + len_3 <= len_1):
    print('not exist')
else:
    if len_1 != len_2 and len_1 != len_3 and len_2 != len_3:
        print('smiple tiangle')
    elif len_1 == len_2 == len_3:
        print('equilateral')
    else:
        print('isosceles')
