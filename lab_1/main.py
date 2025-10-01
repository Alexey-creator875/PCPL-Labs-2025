import sys
import math

NO_ROOTS = 0
ONE_ROOT = 1
TWO_ROOTS = 2
FOUR_ROOTS = 4

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
    coefficientString = sys.argv[index]
    return coefficientString

def ReadCoefficientFromInputStream(index):
    coefficientsLetters = "ABC"
    print(f"Enter coefficient {coefficientsLetters[index - 1]}:")

    coefficientString = input()
    return coefficientString

def CalculateRootsOfQuadraticEquation(a, b, c):
    discriminant = CalculateDiscriminant(a, b, c)

    if discriminant == 0.0:
        rootOfQuadraticEquation = -b / (2.0*a)
        return (ONE_ROOT, rootOfQuadraticEquation)
    elif discriminant > 0.0:
        sqrtDiscriminant = math.sqrt(discriminant)
        root1 = (-b + sqrtDiscriminant) / (2.0*a)
        root2 = (-b - sqrtDiscriminant) / (2.0*a)
        return (TWO_ROOTS, root1, root2)
    else:
        return (NO_ROOTS,)
    
def CalculateDiscriminant(a, b, c):
    return b*b - 4*a*c

def CalculateRootsOfBiquadrateEquation(a, b, c):
    rootsTuple = CalculateRootsOfQuadraticEquation(a, b, c)

    match rootsTuple:
        case (NO_ROOTS,):
            return rootsTuple
        case (ONE_ROOT, root):
            return CalculateBiquadraticRootsForQuadraticRoot(root)
        case (TWO_ROOTS, root1, root2):
            return CalculateBiquadraticRootsIfTwoQuadraticRoots(root1, root2)

def CalculateBiquadraticRootsIfTwoQuadraticRoots(root1, root2):
    rootsTuple1 = CalculateBiquadraticRootsForQuadraticRoot(root1)
    rootsTuple2 = CalculateBiquadraticRootsForQuadraticRoot(root2)

    rootsNumber = rootsTuple1[0] + rootsTuple2[0]

    if (rootsNumber == NO_ROOTS):
        return (NO_ROOTS,)
    elif (rootsNumber == TWO_ROOTS):
        return rootsTuple1 if (rootsTuple1[0] == TWO_ROOTS) else rootsTuple2
    elif (rootsNumber == FOUR_ROOTS):
        return (FOUR_ROOTS, rootsTuple1[1], rootsTuple1[2], rootsTuple1[1], rootsTuple2[2])
        
    
def CalculateBiquadraticRootsForQuadraticRoot(root):
    if root < 0:
        return (NO_ROOTS,)
    elif root == 0:
        return (TWO_ROOTS, 0, 0)
    elif root > 0:
        return (TWO_ROOTS, -math.sqrt(root), math.sqrt(root))
    

def PrintRoots(rootsTuple):
    match rootsTuple:
        case (FOUR_ROOTS, root1, root2, root3, root4):
            print(f"Four roots: {root1}, {root2}, {root3} and {root4}")
        case (TWO_ROOTS, root1, root2):
            print(f'Two roots: {root1} и {root2}')
        case (ONE_ROOT, root):
            print(f'One root: {root}')
        case (NO_ROOTS,):
            print('No roots')        


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

    roots = CalculateRootsOfBiquadrateEquation(a,b,c)
    PrintRoots(roots)

if __name__ == "__main__":
    main()

# Примеры запуска
# python roots_tuple.py 1 0 -4
# Два корня: 2.0 и -2.0

# python roots_tuple.py 1 0 0
# Один корень: -0.0

# python roots_tuple.py 1 0 4
# Нет корней