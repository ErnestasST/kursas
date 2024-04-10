"""
Sukurkite modulį ir importuokite bet kurį pasirinktą PIP paketą. Tada sukurkite funkciją, kuri jį naudotų. Importuokite tą funkciją į main.py modulį ir ją naudokite.
"""

from Stuff.Scripts import joking_around

print("Esu uzd3_08.py Scripts.py", __name__)

x = input("Do you wana hear a joke ?: ")

if x == "yes":
    joking_around()
else:
    quit("Your loss")