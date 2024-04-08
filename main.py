# def multiply(x: int, y: int) -> int:
#
#     sudeti = lambda m,n : m + n
#
#     print(sudeti(m, n))
#
#     return x * y
#
# print(multiply)
#
#
# multication = lambda x, y: x * y
# print(multication)



# text = ['namas', 'aruodas', 'ezeras']
# def check_row_starts(text: list):
#     is_vowel = lambda word: word[0] in "aeiouAEIOU"
#     return [t for t in text if is_vowel(t)]
#
#
# print(check_row_starts(text))


# data = {
#     1: "vienas",
#     2: "du",
#     3: "trys",
# }
#
# def enter_numbers():
#     while True:
#         try:
#             value = int(input("Iveskite skaiciu"))
#             print(data[value])
#         except (ValueError, KeyError, TypeError):
#             raise ValueError("Suvestas ne skaicius")
#         finally:
#             print("spausdiname finally")
#
#
# enter_numbers()


# def enter_numbers():
#     while True:
#         try:
#             value = int(input("Enter a number: "))
#         except ValueError:
#            raise ValueError("suvestas ne skaicius")
#         if value > 10:
#             print("More then 10")
#         else:
#             print("less then 10")
#
#         if value == 15:
#             break



# enter_numbers()

c = 5

def do_something(a, b):
    global c
    d = 7
    def naujas():
        nonlocal d
    print(a, b, c)
    c = 8
    print(c)


do_something(5, 10)
print(c)