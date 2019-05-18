# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
chr_input = int(input('number of chr?\n'))
a = ord('a')
print(f'{chr_input} is {chr(chr_input + a - 1)}')
