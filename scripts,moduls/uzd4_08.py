"""
"Python" modulis os suteikia galimybę naudotis nuo operacinės sistemos priklausančiomis funkcijomis, pvz., skaityti arba rašyti į failų sistemą. Jūsų užduotis yra:

Importuoti os modulį.

Sukurti funkciją, kuri išvardytų visus dabartiniame kataloge esančius failus.

Sukurti funkciją, kuri sukuria naują katalogą.

Sukurti funkciją, kuri pervadina failą.

Sukurkite funkciją, kuri perkelia failą iš vieno katalogo į kitą.

Sukurkite funkciją, kuri ištrina failą.
"""

import os


# os.mkdir(...)
# os.mknod(...)
# os.rename(...)
# os.path.exists(...)
# os.path.join(...)
# os.remove(...)
# os.path

# def name_all_items():# leksografine tvarka
#     return os.listdir()
#
# # ab
# # aaab
#
# print(name_all_items())




# def creating_catalog():
#     return os.mkdir("C:/Users/sem14/Desktop/asdf/testukas")
#
# print(creating_catalog())
#

# def renaming():
#     return os.rename("C:/Users/sem14/Desktop/asdf/testukas", "C:/Users/sem14/Desktop/asdf/testas")

# print(renaming())



def removing_file():
    # os.path.join("C:""Users", "sem14", "Desktop", "asdf")
    os.remove("C:""Users", "sem14", "Desktop", "asdff")


removing_file()









