# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import funktions as f

numbers = f.create_list_number_fl_random(5)
print(numbers)
largest = 0
smallest = int(str(numbers[0]).split('.')[1])

for i in numbers:
    if int(str(i).split('.')[1]) > largest:
        largest = int(str(i).split('.')[1])
    if int(str(i).split('.')[1]) < smallest:
        smallest = int(str(i).split('.')[1])

print(f'Максимальное значение дробной части элементов {largest / 100}')
print(f'Минимальное значение дробной части элементов {smallest / 100}')
print(f'Разница {(largest - smallest) / 100}')