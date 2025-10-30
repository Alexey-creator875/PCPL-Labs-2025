from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FColor import FColor


class Rectangle(GeometricFigure):
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = FColor(color)

    def area(self):
        return self.width * self.length
    
    def __repr__(self):
        return 'Width: {}, Length: {}, Color: {}, Area: {}'.format(self.width, self.length, self.color.color, self.area())
    
