"""This module calculates the areas of various shapes.
Requiers python 3.10 or higher."""
from math import pi, sqrt

class Circle():
    def __init__(self, radius: int | float):
        self.radius = radius
        
        self.area = self.radius ** 2 * pi

class Triangle():
    def __init__(self, side_1: int | float, side_2: int | float, side_3: int | float):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

        self.perimeter = self.side_1 + self.side_2 + self.side_3
        semiperimeter = self.perimeter / 2
        self.area = sqrt(semiperimeter
                    * (semiperimeter - self.side_1)
                    * (semiperimeter - self.side_2)
                    * (semiperimeter - self.side_3))
        
        if (side_1**2 + side_2**2 == side_3**2)\
        or (side_1**2 + side_3**2 == side_2**2)\
        or (side_3**2 + side_2**2 == side_1**2):
            
            self.is_right = True 
        else:
            self.is_right = False