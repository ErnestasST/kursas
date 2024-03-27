"""
Sukurkite programą, kuri leistų naudotojui įvesti skaičių seriją ir apskaičiuotų visų skaičių vidurkį. Programa taip pat turėtų išspausdinti visų skaičių list'a ir vidurkį.
"""

number_score = 0
input_count = 0
listas = []

# while True:
#     number = (input("enter a number: "))
#     input_count += 1
#     number_score += int(number)
#     print([number_score / input_count])

for i in range(5):
    number = (input("enter a number: "))
    input_count += 1
    number_score += int(number)
    listas.append(number)

print(listas, [number_score / input_count])


