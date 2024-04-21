# """
# Sukurti klasę, kurioje atributas butu "text".
#
# Sukurti metodus, kurie:
# 	1. Suskaičiuotų kiek yra žodžių tekste;
# 	2. Metoda, kuris gražintų visus žodžius, kurie būtų nurodyti metodo kintamajame.
# 	Pvz nurodytos raidės 'ams', turi išrinkti visus žodžius, kurie turis šias raides.
# 	3. Išrinktų visus žožius, kurių ilgis didesnis arba lygus nurodytam metode;
#
# Prasau pagalvoti ar Jūsų sprendime nėra kodo dubliavimo ir pagalvokite kaip jo išvengti
#
# """
#
#class Text:
#     def __init__(self, text: str):
#         self.text = text
#
#     def split_text(self):
#         return self.text.split()
#
#     def count_words(self) -> int:
#         return len(self.split_text())
#
#     def return_words_with_letters(self, letters: str ='ams') -> list:
#         result = []
#         for word in self.split_text():
#             if all(letter in word for letter in letters):
#                 result.append(word)
#         return result
#
#     def return_longer_than_number(self, number: int = 5) -> list:
#         return [word for word in self.split_text() if len(word) > number]

# class Animal(object):
#     def __init__(self, age: int, callor: str):
#         self.age = age
#         self.callor = callor
#
#     def eat(self):
#         print("Eats")
#
#     # def make_sounds(self):
#         print("make sounds")
#
# class Bird(Animal):
#     def __init__(self, age, callor, type: str = "waterbird"):
#         self.callor = "brown"
#         super().__init__(age, callor)
#         self.type = type
#
#     def fly(self):
#         print("bird flies")
#
#     def make_sounds(self):
#         print("make sounds")
#
#
# class Mammoth(Animal):
#     def __init__(self, age: int, callor: str):
#         super().__init__(age, callor)
#
#     def walk(self):
#         print("walk very fast")
#
#
#     def _protected_method(self):
#         print("protected method")
#
#
# bird = Bird(10, "yellow")
# print(bird.age)
#
#
# mamutas = Mammoth(185, "green")
# print(mamutas.callor)
#

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def create_sound(self):
        pass

class TV(Device):
    def __init__(self):
        self.a = 5

    def turn_on(self):
        print("Trun on device")

    def turn_off(self):
        print("turn off")

    def create_sound(self):
        print("created sound")


tv = TV()
print(tv.turn_on())
