"""
Sukurkite Calculator klasę su pagrindinėmis funkcijomis: sudėti, dalyti, dauginti, atimti ir t. t.. Inicijuokite klasę ir parodykite keletą skaičiavimų.
"""

class Calculator(int):
    def __int__(self) -> int:
        pass
    def add(self,num1: int, num2: int) ->int:
        return num1 + num2
    def subs(self,num1: int, num2: int) ->int:
        return num1 - num2
    def div(self,num1: int, num2: int) ->int:
        return num1 % num2
    def mult(self,num1: int, num2: int) ->int:
        return num1 * num2


print("sum", Calculator.add(self=Calculator, num1=5, num2=5))
print("subs", Calculator.add(self=Calculator, num1=2, num2=6))
print("div", Calculator.add(self=Calculator, num1=6, num2=2))
print("mult", Calculator.add(self=Calculator, num1=2, num2=8))