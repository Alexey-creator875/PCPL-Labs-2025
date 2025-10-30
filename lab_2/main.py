from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle


NUMBER_IN_STUDENT_LIST = 20

def main():
    rectangle = Rectangle(NUMBER_IN_STUDENT_LIST, NUMBER_IN_STUDENT_LIST, "blue")
    print("Rectangle", rectangle, sep='\n')

    circle = Circle(NUMBER_IN_STUDENT_LIST, "green")
    print("Circle", circle, sep='\n')

    
if __name__ == "__main__":
    main()
