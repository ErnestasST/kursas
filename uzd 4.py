"""
stringas = "Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius, skaičių"
"""

stringas = "Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e"


def count_words_that_have_5_or_more_simbols():
    score = 0
    for word in stringas.split():
        if len(word) >= 5:
            score += 1
    return score

print(count_words_that_have_5_or_more_simbols())

