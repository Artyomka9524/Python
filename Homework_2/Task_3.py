# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

number = int(input("Введите N: "))
list_number = [round(((1+1/i)**i), 3) for i in range(1, number+1)]
print(F"Последовательность: {list_number}")
sum_numbers = 0
for i in range(0, len(list_number)):
    sum_numbers += list_number[i]
print(f"Сумма чисел последовательности = {sum_numbers}")