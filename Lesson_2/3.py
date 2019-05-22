"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

# с помощью функций

num = int(input('введите число: '))
result = ''
while True:
    res1 = num % 10
    res2 = num // 10
    if res2 == 0:
        result += str(res1)
        break
    else:
        num = res2
        result += str(res1)

print(result)


# с помощью рекурсии

def mirror(num, result):

    res1 = num % 10
    res2 = num // 10
    if res2 == 0:
        result += str(res1)
    else:
        num = res2
        result += str(res1)
        return mirror(res2, result)
    print(result)


num_f = int(input('введите число: '))
result_f = ''
mirror(num_f, result_f)
