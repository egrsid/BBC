def calc_sum(num1: float, num2: float) -> float:
    """returns the sum of two numbers"""
    return num1 + num2

def calc_diff(num1: float, num2: float) -> float:
    """returns the diff of two numbers"""
    return num1 - num2

def calc_mul(num1: float, num2: float) -> float:
    """returns the mul of two numbers"""
    return num1 * num2

def calc_div(num1: float, num2: float) -> float:
    """returns the div of two numbers"""
    return num1 / num2


num1 = float(input("Введите число 1: "))
num2 = float(input("Введите число 2: "))

operation = str(input("введите операцию, которую хотите сделать: 1 - сложение, 2 - вычитание, 3 - уножение, 4 - деление: "))

if operation == '1': print(calc_sum(num1, num2))
elif operation == '2': print(calc_diff(num1, num2))
elif operation == '3': print(calc_mul(num1, num2))
else : print(calc_div(num1, num2))