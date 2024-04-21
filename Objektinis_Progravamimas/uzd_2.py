"""
Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas). Turint asmens vardą ir pavardę:

Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę, atskiriamus tarpeliu.

Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį . Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.
"""

class Canditats:
    def __init__(self, name: str, surname: str):
        self.name = name.join(surname)
        self.fullname = name + " " + surname
        self.email = name.lower() + "_" + surname.lower() + "@email.com"



f_person = Canditats("Mike", "Mykolson")


print(f_person.fullname)
print(f_person.email)
