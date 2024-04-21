"""
Sukurkite keletą savo pavyzdžių, kuriuose parodytumėte ir panaudotumėt keletą OOP paradigmų praktikoje.
"""

class Book:
    def __init__(self, author: str, name: str):
        self.author = author
        self.name = name

    def info(self):
        print(f"Book {self.name}, Books author {self.author}")

book1 = Book("Chuck Shurley", "Supernatural")

print(book1.info())