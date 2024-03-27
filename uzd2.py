"""
eiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.
"""

numbers_score = 0

for i in range(0,11):
    numbers = int(input("Iveskite sveikuosius skaicius"))
    numbers_score += numbers
print(numbers_score, numbers_score/10)
