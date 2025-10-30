from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


NUMBER_IN_STUDENT_LIST = 20

def main():
    rectangle = Rectangle(NUMBER_IN_STUDENT_LIST, NUMBER_IN_STUDENT_LIST, "blue")
    print(rectangle.getFigureType())
    print(rectangle)

    circle = Circle(NUMBER_IN_STUDENT_LIST, "green")
    print(circle.getFigureType())
    print(circle)

    square = Square(NUMBER_IN_STUDENT_LIST, "red")
    print(square.getFigureType())
    print(square)

    
if __name__ == "__main__":
    main()
