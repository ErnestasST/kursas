

stringas = "Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e"

def score_e_words():
    words = stringas.split()
    score = 0
    for word in words:
        if 'e' in word:
            score += 1
    return score

print(score_e_words())
