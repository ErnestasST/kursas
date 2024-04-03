"""
Parašykite funkciją, kuri paima du list'us ir prie pirmojo list pirmojo elemento prideda antrojo listpirmąjį elementą, antrojo sąrašo antrąjį elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo antrąjį elementą. pirmąjį sąrašą su antruoju antrojo sąrašo elementu ir t. t., ir t. t. Grąžinkite True, jei visi elementų deriniai sudaro tą patį skaičių. Priešingu atveju grąžinama False. Pavyzdys:
"""

def sum_lists(a=list, b=list) ->bool:
    if len(a) == len(b):
        sum_list = []
        for index, value in enumerate(a):
            sum_list.append(value + b[index])
        return len(sum_list)/len(sum_list) == sum_list[0]
    return False


print(sum_lists(a=[1, 8, 5, 8, -1, 7], b=[0, -7, -4, 1, 2, -6]))



