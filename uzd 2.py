"""
Raskite visus skaičius iš 1-1000, kuriuose yra 9.
"""

def find_which_have_9_init():
    return [number for number in range(1,1001) if "9" in str(number)]

print(find_which_have_9_init())



