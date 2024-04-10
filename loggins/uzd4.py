"""
Sukurkite programą, kuri priima 4 duomenų tipus/struktūras: strings, numbers, list, dict. Iteriuokite 10 kartų su įvestimis ir užregistruokite, koks duomenų tipas/struktūra ir kiek kartų buvo įvesta. Apdorokite visas galimas klaidas ir jas užregistruokite.
"""


import logging

logging.basicConfig(filename="Counting.txt", level=logging.WARNING,format="%(asctime)s - %(name)s - %(message)s - %(levelname)s",datefmt="%d/%m/%y %H:%M:%S")

date = {
    "one": 1,
    "two": 2,
    "three": 3
}


digi = "words"
items = ["socks", "shoes"]
num = 5


for x in range(0,11):
    
    logging.error(date)
    logging.error(digi)
    logging.error(items)
    logging.error(num)