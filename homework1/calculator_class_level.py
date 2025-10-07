import math

class Calculator():
    def __init__(self, num1: float, num2: float) -> None:
        self.num1 = num1
        self.num2 = num2

    def calc_sum(self) -> float:
        return self.num1 + self.num2
    
    def calc_diff(self) -> float:
        return self.num1 - self.num2
    
    def calc_mul(self) -> float:
        return self.num1 * self.num2
    
    def calc_div(self) -> float:
        return self.num1 / self.num2

    def calc(self, operation: str) -> float:
        if operation == '1': return self.calc_sum()
        elif operation == '2': return self.calc_diff()
        elif operation == '3': return self.calc_mul()
        else: return self.calc_div()

    def smart_calc(to_solve: str) -> float:
        return eval(to_solve)
    
class Engineer(Calculator):
    def __init__(self, num1: float, num2: float) -> None:
        self.num1 = num1
        self.num2 = num2
        self.main_num = num1

    def select_num(self, n: int) -> None:
        """1 - num1; 2 - num2"""
        self.main_num = num1 if n == '1' else num2

    def calc_sin(self) -> float:
        return float(math.sin(self.main_num))
    
    def calc_cos(self) -> float:
        return float(math.cos(self.main_num))


num1 = float(input("Введите число 1: "))
num2 = float(input("Введите число 2: "))

operation = str(input("введите операцию, которую хотите сделать: 1 - сложение, 2 - вычитание, 3 - уножение, 4 - деление: "))

calc_obj = Calculator(num1, num2)
calc_obj_eng = Engineer(num1, num2)

print(calc_obj.calc(operation))
calc_obj_eng.select_num('1')
print(calc_obj_eng.calc_sin())