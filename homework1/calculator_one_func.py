def calc(num1: float, num2: float, operation: str) -> float:
    if operation == '1': return float(num1 + num2)
    elif operation == '2': return float(num1 - num2)
    elif operation == '3': return float(num1 * num2)
    else: return float(num1 / num2)

num1 = float(input("Введите число 1: "))
num2 = float(input("Введите число 2: "))

operation = str(input("введите операцию, которую хотите сделать: 1 - сложение, 2 - вычитание, 3 - уножение, 4 - деление: "))

print(calc(num1, num2, operation))