# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_values(x):
    a = [0] * x
    for i in range(x):
        correctly = False
        while not correctly:
            try:
                number = float(input(f'Введите {i+1} координату: '))
                a[i] = number
                correctly = True
                if a[i] == 0:
                    correctly = False
                    print('По условию значение координаты не равен 0 ')
            except ValueError:
                print('Похоже, что это не число, проверь.')
    return a


def checking_coordinates(xy):
    surface = 4
    if xy[0] > 0 and xy[1] > 0:
        surface = 1
    elif xy[0] < 0 and xy[1] > 0:
        surface = 2
    elif xy[0] < 0 and xy[1] < 0:
        surface = 3
    print(f'Точка в {surface} четверти плоскости')


coordinate = input_values(2)
checking_coordinates(coordinate)
