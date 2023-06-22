'''вычислить площадь круга и длину окружности по диаметру'''
import math
from _pydecimal import getcontext
from decimal import Decimal
getcontext().prec = 43

s_circle = 0       # площадь круга, 42 зн после ,
circumference = 0  # длина окружности
r = 0              # радиус

d = float(input('Введите диаметр круга(не более 1 000): '))
if 0 < d <= 1000:
    r = d / 2
    s_circle = math.pi * r ** 2
    circumference = d * math.pi
    print(f'Площадь круга равна {Decimal(s_circle)}, длина окружности равна {Decimal(circumference)}.')
