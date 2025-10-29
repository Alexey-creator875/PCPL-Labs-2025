from GeometricFigure import GeometricFigure
from FColor import FColor


class Rectangle(GeometricFigure):
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = FColor(color)

    def area(self):
        return self.width * self.length
