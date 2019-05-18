# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

chr_1 = ord(input('chr_1 = '))
chr_2 = ord(input('chr_2 = '))
a = ord('a')

place_chr_1 = chr_1 - a + 1
place_chr_2 = chr_2 - a + 1

between_chr_1_and_chr_2 = abs(place_chr_2 - place_chr_1)
between_chr_1_and_chr_2 = between_chr_1_and_chr_2 if between_chr_1_and_chr_2 == 0 else between_chr_1_and_chr_2 - 1

print(f'{place_chr_1} {place_chr_2} {between_chr_1_and_chr_2}')
