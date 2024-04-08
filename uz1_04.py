"""
Sukurkite bent 5 skirtingas funkcijas ir pabandykite apdoroti bent 5 integruotas "Python" išimtis.
"""

def sum_numbers(a, b):
    try:
        result = int(a) + int(b)
        return result
    except:
        print("invalid syntax")

print(sum_numbers("MOM", "DAD"))


def div_sum(q, w):
    try:
        result = int(q) / int(w)
        return result
    except ZeroDivisionError:
        print("Cannot divide whit 0")

print(div_sum(5, 0))



def extracting_a_letter(text, contrainer):
    try:
        list1 = text[contrainer]
        return list1
    except IndexError:
        print("Out of index")

print(extracting_a_letter("word", 5))


def change_str_to_int(str):
    try:
        number = int(str)
        return number
    except ValueError:
        print("You cannot change to int")

print(change_str_to_int("abc"))


def div_sum(q, w):
    try:
        result = int(q) / int(w)
        return result
    except TypeError:
        print("you cant divide a letter")

print(div_sum(8, id))