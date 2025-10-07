num1 = float(input("Введите число 1: "))
num2 = float(input("Введите число 2: "))

operation = str(input("введите операцию, которую хотите сделать: 1 - сложение, 2 - вычитание, 3 - уножение, 4 - деление: "))

if operation == '1': print(num1 + num2)
elif operation == '2': print(num1 - num2)
elif operation == '3': print(num1 * num2)
else: print(num1 / num2)