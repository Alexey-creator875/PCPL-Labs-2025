from lab_python_oop.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length, color):
        super().__init__(length, length, color)

    def area(self):
        return self.width * self.length
    
    def __repr__(self):
        return 'Length: {}; Color: {}; Area: {}'.format(self.length, self.color.color, self.area())
    
