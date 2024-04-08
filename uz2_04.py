"""
Python kalboje, dalijant iš nulio, gauname ZeroDivisionError. Jūsų užduotis - sukurti funkciją, kuri:

Kaip argumentus priima du skaičius.

Mėgina padalyti pirmąjį skaičių iš antrojo.

Jei antrasis skaičius yra nulis, ji turėtų sugauti ZeroDivisionError ir grąžinti pasirinktinį klaidos pranešimą.

Jei dalijimas sėkmingas, turėtų būti grąžinamas rezultatas.

Nepriklausomai nuo to, ar dalijimas pavyko, ar ne, turėtų būti išspausdintas pranešimas "Attempted division". Jei įvesties duomenys nėra skaičiai, pateikiamas TypeError pranešimas. Funkcija pagauna šią TypeError ir grąžina pasirinktinį klaidos pranešimą.
"""

def divide_numbers(a, b):
    try:
        result = a/b
        print("Trying to divide")
        return result
    except ZeroDivisionError:
        return ("You cannot divide whit 0")
    except TypeError:
        return ("Something is wrong")

print(divide_numbers(25, 5))
print(divide_numbers(91, 0))
print(divide_numbers(1, id))
