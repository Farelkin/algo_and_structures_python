# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = int(input('введите 3х значное число\n'))

# если введенное число 123, то
digit_last = number % 10  # = 3
digit_center = number % 100 // 10  # = 2
digit_first = number // 100  # = 1

print(f'сумма чисел в введенном числе равна {digit_first + digit_center + digit_last}')
print(f'произведение числе в введенном числе равна {digit_first * digit_center * digit_last}')
