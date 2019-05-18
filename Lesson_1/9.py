# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

num1 = int(input('num 1\n'))
num2 = int(input('num 2\n'))
num3 = int(input('num 3\n'))

if num1 == num2 ==num3:
    print(f'middle num = {num1}')
elif num2 < num1 > num3:

    if num2 > num3:
        print(f'middle num = {num2}')
    else:
        print(f'middle num = {num3}')

elif num2 < num1 < num3:
    print(f'middle num = {num1}')

elif num2 > num1 < num3:

    if num2 > num3:
        print(f'middle num = {num3}')
    else:
        print(f'middle num = {num2}')
