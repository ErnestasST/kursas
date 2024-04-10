"""
Sukurkite apskaitos programą, kuri paimtų metines pajamas, išlaidas, PVM tarifą (visos reikšmės turi būti kintamos) ir apskaičiuotų pelną, sumokėtus mokesčius 4 skirtingomis valiutomis (USD, EU, JPY, CNY). Visi skaičiavimai ir rezultatai turėtų būti spausdinami ekrane. Visi duomenys ir galimos klaidos turi būti registruojami į failą.
"""

import logging

logging.basicConfig(
    filename="Data.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s - %(levelname)s",
    datefmt="%d/%m/%y %H:%M:%S"
)

# CRITICAL, ERROR, WARNING, INFO, DEBUG
# CRITICAL - SVARBU
# DEBUG - MAZIAUSIAI SVARBU
