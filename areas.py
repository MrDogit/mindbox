"""This module calculates the areas of various shapes"""

"""
Задание:

Напишите на C# или Python библиотеку для поставки внешним клиентам, 
которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. 
Дополнительно к работоспособности оценим:

- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным
"""
from math import pi, sqrt

def circle(radius:int)->int:
    return radius ** 2 * pi

def triangle(side_1:int, side_2:int, side_3:int) -> int:
    perimeter = side_1 + side_2 + side_3
    area = side_1 + side_2 + side_3
    area = sqrt(perimeter
                * (perimeter - side_1)
                * (perimeter - side_2)
                * (perimeter - side_3))
    return area