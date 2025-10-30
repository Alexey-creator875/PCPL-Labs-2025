from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FColor import FColor
from math import pi


class Circle(GeometricFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FColor(color)

    def area(self):
        return pi * self.radius * self.radius
    
    def __repr__(self):
        return 'Radius: {}; Color: {}; Area: {}'.format(self.radius, self.color.color, self.area())
    
