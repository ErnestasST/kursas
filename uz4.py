"""
Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.
"""

def extract_uniq_string(stringas):
    uniq_stringas = []
    for strings in stringas.split():
        if len(strings) == len(set(strings)):
            uniq_stringas.append(strings)
    return uniq_stringas

stringas = "Vestibulum@example.net eu dolor non leo lacinia tincidunt. Fusce tristique lacus nec mauris fermentum"

a = extract_uniq_string(stringas)
print(a)