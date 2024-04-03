"""
priima du argumentus: eilutę ir skaičių.

grąžina naują eilutę, kuri pakartoja pradinę eilutę tiek kartų, kiek kartų pakartotas skaičius. Pavyzdžiui, jei įvesties duomenys yra Hello ir 3, funkcija turėtų grąžinti HelloHelloHello.
"""


def repeating_word(word, number):
    return word * number


word = (input("Enter a word: "))
number = int(input("Enter a letter: "))

a = repeating_word(word, number)
print(a)
