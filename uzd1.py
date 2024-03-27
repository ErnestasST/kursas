"""
Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį. Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį. Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą.
"""

while True:
    name = str(input("Type name: "))
    password = str(input("type you password: "))
    if name == "Julius" and password == "Julevivius":
        print(f"Hello {name}, {password}")
        break
