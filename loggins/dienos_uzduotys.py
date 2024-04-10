import copy

# def clearing(date: dict, nesessary_key: list,deleting_key ):
#
#
#     result_n = {}
#     new_date = copy.deepcopy(date)
#     for key in date:
#         if key in nesessary_key:
#             result_n[key] = date[key]
#         if key in deleted_key:
#             del new_date[key]
#
#     return result_n, new_date
#
#
# numbers = {
#     1: "vienas",
#     2: "du",
#     3: "trys",
#     4: "keturi"
# }
# needed_key = [1, 2]
#
# deleted_key = [3]
#
# print(clearing(date=numbers, nesessary_key=needed_key, deleting_key=deleted_key))
#



# import math
#
# def distracting_number(numbers: list, number: int):
#     value = math.ceil(len(numbers)//number)
#     return [numbers[x * number:x * number + number] for x in range(value)]
#     # result = []
#     # for x in range(value):
#     #     first_index, second_index = x * number, x * number + number
#     #     result.append(number[first_index:second_index])
#     # return result
#
#
# date = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# repeating = 3

# print(distracting_number(numbers=date, number=repeating))



import logging
from time import time

date = time()
filename = f"{date}_date log"
logging.basicConfig()

def cal(*args):
    result = {"lyginis": 0, "Nelyginis": 0}
    for x in args:
        if x % 2 == 0:
            result["lyginis"] += 0
            logging.info(f'{x} pridetas prie Lyginio')
        else:
            result["Nelyginis"] += 0
            logging.info(f'{x} pridetas prie Nelyginio')

    logging.info(f'grazinimo reiksme {result}')
    return result

numbers = [1, 2, 3, 4, 5, 6, 0]
print(cal(*numbers))







