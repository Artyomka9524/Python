# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

numbers = list(input("Введите число: "))
sum_numbers = 0

for i in range(0, len(numbers)):
    if numbers[i] != "." and numbers[i] != "-":
        sum_numbers += int(numbers[i])

print(f"Сумма цифр числа: {sum_numbers}")