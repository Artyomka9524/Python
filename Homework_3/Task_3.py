# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

import funktions as f

user_number = f.check_input_number('Введите целое число: ')
save_number = user_number
binary_number = 0
ten = 1

while abs(user_number) > 0:
    binary_number += (abs(user_number) % 2) * ten
    user_number = abs(user_number) // 2
    ten *= 10

if save_number > 0:
    print(int(binary_number))
elif save_number < 0:
    print(-int(binary_number))