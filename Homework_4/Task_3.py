# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

from random import randrange

def list_random_numbers(count: int):
    if count < 0:
        print("Отрицательное значение количества чисел")
        return []

    list_numbers = []
    for i in range(count):
        list_numbers.append(randrange(count))

    return list_numbers

def un_el(list_numbers: list):
    result = []
    dictionary = {}.fromkeys(list_numbers, 0)

    for i in list_numbers:
        dictionary[i] += 1

    for k in dictionary:
        if dictionary[k] == 1:
            result.append(k)

    return result

list = list_random_numbers(int(input("Количество чисел: ")))
print(list)
print(un_el(list))
