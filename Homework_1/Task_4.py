# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите порядковый номер четверти: '))
while not 1 <= quarter <= 4:
    quarter = int(input('Введено неверное значение'))
if quarter == 1:
    print('X(0, +∞) Y(0, +∞)')
elif quarter == 2:
    print('X(-∞, 0) Y(0, +∞)')
elif quarter == 3:
    print('X(-∞, 0) Y(-∞, 0)')
elif quarter == 4:
    print('X(0, +∞) Y(-∞, 0)')