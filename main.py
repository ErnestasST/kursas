# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)
#
# number = range(10)
# squares = [number * number for number in number if number % 2 == 0]
#
# print(squares)
#
#
# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])
#
#

# squares = {i: i * i for i in range(10)}
# print(squares)

# squares = {key: value for key, value in enumerate(range(10, 20))}
# print(squares)
#
# for key, value in enumerate(range(10, 20)):
#     print(f" key {key}:, Value {value}:")


# function = "5 + 8 + 9 + 14"
# print(eval(function))

# map/filter
date_1 = [2, 4, 6, ]
date_2 = [1, 3, 5]

def dauginti(x):
    return x * x

print(list(map(dauginti, date_1)))
print([dauginti(x) for x in date_1])