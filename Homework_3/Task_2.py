# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

import funktions as f

numbers = f.create_list_number_random(9)
print(numbers)
multiplication = 1
if len(numbers) % 2 == 0:
    for i in range(len(numbers) // 2):
        multiplication = numbers[i] * numbers[len(numbers) - i - 1]
        print(f'{numbers[i]} * {numbers[len(numbers) - i - 1]} = {multiplication}')
else:
    for i in range(len(numbers) // 2):
        multiplication = numbers[i] * numbers[len(numbers) - i - 1]
        print(f'{numbers[i]} * {numbers[len(numbers) - i - 1]} = {multiplication}')
    multiplication = numbers[len(numbers) // 2] * numbers[len(numbers) // 2]
    print(f'{numbers[len(numbers) // 2]} * {numbers[len(numbers) // 2]} = {multiplication}')

