# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample

def more_then(num):
    list = sample(range(num * 3), num)
    print(list)
    return [list[num] for num in range(1, len(list)) if list[num] > list[num - 1]]

print(more_then(int(input("Введите элементы исходного списка: "))))    