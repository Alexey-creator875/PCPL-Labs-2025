import sys
import math

def ReadCoefficient(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coefficientString = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coefficientString = input()
    # Переводим строку в действительное число
    coef = float(coefficientString)
    return coef

def ReadCoefficientFromCommandLine(index):
    coefficientString = sys.argv(index)
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
    '''
    Основная функция
    '''
    a = ReadCoefficient(1, 'Введите коэффициент А:')
    b = ReadCoefficient(2, 'Введите коэффициент B:')
    c = ReadCoefficient(3, 'Введите коэффициент C:')
    # Вычисление корней
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