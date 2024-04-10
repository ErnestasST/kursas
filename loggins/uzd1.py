"""
Sukurkite paprastą programą, kuri registruotų (logs) visus įvesties duomenis iš terminalo. Konfigūracijose turi būti rodomi visi papildomi duomenys (laikas, data, lygis ir t. t.).
"""

import logging


a = logging.basicConfig(filename="logs.txt", level=logging.INFO,format="%(asctime)s - %(name)s - %(message)s - %(levelname)s",datefmt="%d/%m/%y %H:%M:%S")

test = (1, 4, 5, "a", 5.66)
logging.info(test)



