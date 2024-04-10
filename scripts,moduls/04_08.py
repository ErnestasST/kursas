# def dividing(list1, number):
#     result = []
#     for lnumber in list1:
#         if lnumber % number == 0:
#             result.append(lnumber)
#     return result
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# number = 2
#
#
# print(dividing(list1, number))



"""
Parašyti funciją, į kurią padavus skaičių atspausdintų tokia tvarka kaip parodyta žemiau. Funkcija turi priimti 2 variable – nuo kurio iki kurio skaiciaus.:
"""

# def lining_numbers(first_number, second_number):
#
#     for x in range(first_number, second_number + 1):
#         print(str(x) * x)
#
# f_number = 3
# sec_number = 5
#
# print(lining_numbers(f_number, sec_number))



"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order. 

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits. 
"""


# def extracting(numbers):
#     rev_number = []
#     change = str(numbers)
#
#     for extraction in change[::-1]:
#         rev_number.append(extraction)
#     return " ".join(rev_number)
#
# number =  7536
# print(extracting(number))



"""
 Exercise 13: Print multiplication table from 1 to 10 

Expected Output: 

1  2 3 4 5 6 7 8 9 10 		 
2  4 6 8 10 12 14 16 18 20 		 
3  6 9 12 15 18 21 24 27 30 		 
4  8 12 16 20 24 28 32 36 40 		 
5  10 15 20 25 30 35 40 45 50 		 
6  12 18 24 30 36 42 48 54 60 		 
7  14 21 28 35 42 49 56 63 70 		 
8  16 24 32 40 48 56 64 72 80 		 
9  18 27 36 45 54 63 72 81 90 		 
10 20 30 40 50 60 70 80 90 100 
"""


for x in range(1, 11):
    tablet = []
    for y in range(1, 11):
        tablet.append(x * y)
    print(" ".join(str(x) for x in tablet))



"""
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk) 
* * * * *   
"""

def star_printing(stars):
    for shine in range(stars,  0, -1):
        print("*" * shine)

star_printing(8)