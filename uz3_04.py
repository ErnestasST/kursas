"""
Sukurkite mini "Python" programą, kuri įvestų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą. Tvarkykite visas galimas klaidas.
"""


def calculation(num1, num2):
    try:
        sum_result = num1 + num2
        subtraction_result = num1 - num2
        multiplication_result = num1 * num2
        division_result = num1 / num2
        return sum_result, subtraction_result, multiplication_result, division_result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result, subtraction_result, multiplication_result, division_result = calculation(num1, num2)

    print("Sum:", sum_result)
    print("Subtraction:", subtraction_result)
    print("Multiplication:", multiplication_result)
    print("Division:", division_result)

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
