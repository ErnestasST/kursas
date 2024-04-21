"""
Sukurkite knygos klasę Book, kuri turi du atributus:

name

author

ir du metodus:

Metodas, pavadintas .get_title(), kuris grąžina: "Pavadinimas: " + egzemplioriaus pavadinimas.

Metodas .get_autor(), kuris grąžina: "Autorius: " + egzempliorius autorius.

ir instancuokite šią klasę sukurdami 3 naujas knygas:


- Pride and Prejudice - Jane Austen (PP)
- Hamletas - Viljamas Šekspyras (H)
- Karas ir taika - Levas Tolstojus (WP)
Naujų egzempliorių pavadinimai turėtų būti atitinkamai PP, H ir WP. Pavyzdžiui, jei, naudodamas šią knygų klasę, instancuočiau šią knygą:


- Haris Poteris - J. K. Rowling (HP)
Gaučiau šiuos atributus ir metodus:


HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Pavadinimas: Haris Poteris"
HP.get_author() ➞ "Autorius: Rowling"
"""

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_title(self):
        return "Book: " + self.name

    def get_author(self):
        return "Author: " + self.author

PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamletas", "Viljamas Šekspyras")
WP = Book("Karas ir taika", "Levas Tolstojus")

print(PP.get_title())
print(H.name)
print(WP.get_author())




