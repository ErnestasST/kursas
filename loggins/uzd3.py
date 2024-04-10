"""
Sukurkite 3 funkcijas, kurios yra susijusios viena su kita (viena iškviečiama kitoje), ir išbandykite visus logging sunkumo lygius pagal savo projektą.

Funkcijų pavyzdžiai:

def check_engine() -> None:
  pass

def start_car() -> None:
  check_engine()...
.......
"""

import logging

logging.basicConfig(filename="Car.txt", level=logging.WARNING,format="%(asctime)s - %(name)s - %(message)s - %(levelname)s",datefmt="%d/%m/%y %H:%M:%S")
#

def check_engine():
    logging.warning("Opening car hood, checking oil level")
    logging.warning("Oil level if fine")
    pass

def start_car():
    check_engine()
    logging.warning("Opening cars door and sitting in to it")
    logging.warning("Engine starts fine")
    pass

def start_moving():
    start_car()
    logging.warning("Shift R gear and start moving from the garage ")
    logging.warning("Shift D and start to enjoy the ride")


print(start_moving())





