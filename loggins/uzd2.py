"""
Parašykite funkciją, kuri perkeltų visus vieno tipo elementus į list galą:

move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
Registruokite įvestis ir rezultatus į failą.
"""

import logging

def move_to_end(numbers: list, number: int):
    quantity = numbers.count(number)
    return [n for n in numbers if n != number] + [number for _ in range(quantity)]


move = [1, 3, 2, 4, 4, 1]
uno = 1

print(move_to_end(numbers=move, number=uno))

logging.info(move_to_end(numbers=move, number=uno))


