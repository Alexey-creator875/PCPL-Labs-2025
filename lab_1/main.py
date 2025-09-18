import sys
import math

def GetCoefficient(index):
    coefficientString = ReadCoefficient(index)

    try:
        coefficient = float(coefficientString)
        return (True, coefficient)
    except:
        return (False, None)

def ReadCoefficient(index):
    try:
        coefficientString = ReadCoefficientFromCommandLine(index)
    except:
        coefficientString = ReadCoefficientFromInputStream(index)
    return coefficientString


def ReadCoefficientFromCommandLine(index):
    coefficientString = sys.argv(index)
    return coefficientString

def ReadCoefficientFromInputStream(index):
    if index == 1:
        print("Enter coefficient A:")
    elif index == 2:
        print("Enter coefficient B:")
    elif index == 3:
        print("Enter coefficient C:")
    else:
        print("Invalid index")

    coefficientString = input()
    return coefficientString

def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        Список корней в форме кортежа
    '''
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        return ('OneRoot', root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        return ('TwoRoots', root1, root2)
    else:
        return ('NoRoots',)


def print_roots(roots_tuple):
    '''
    Печать корней квадратного уравнения

    Args:
        Список корней в форме кортежа
    '''
    match roots_tuple:
        case ('TwoRoots', root1, root2):
            print(f'Два корня: {root1} и {root2}')
        case ('OneRoot', root):
            print(f'Один корень: {root}')
        case ('NoRoots',):
            print('Нет корней')        


def main():
    validCoefficient, a = GetCoefficient(1)

    if not validCoefficient:
        print("Invalid coefficient")
        return


    validCoefficient, b = GetCoefficient(2)

    if not validCoefficient:
        print("Invalid coefficient")
        return

    validCoefficient, c = GetCoefficient(3)

    if not validCoefficient:
        print("Invalid coefficient")
        return

    roots = get_roots(a,b,c)
    # Вывод корней
    print_roots(roots)


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Примеры запуска
# python roots_tuple.py 1 0 -4
# Два корня: 2.0 и -2.0

# python roots_tuple.py 1 0 0
# Один корень: -0.0

# python roots_tuple.py 1 0 4
# Нет корней