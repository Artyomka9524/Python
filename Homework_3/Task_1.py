# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

def create_list_number_random(size):
    from random import randint
    list_number = [randint(1, 50) for _ in range(size)]
    return list_number

size_list = int(input('Введите размер списка: '))

numbers = create_list_number_random(size_list)

total = 0
print(numbers)
for i in range(len(numbers)):
    if i % 2 == 0:
        total += numbers[i]
print(f'Сумма элементов списка, стоящих на нечётных позициях: {total}')