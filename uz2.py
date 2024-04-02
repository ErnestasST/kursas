"""
Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.
"""

def add_string(value, end_string = "string"):
    return [f"{d}_{end_string}" for d in value]

date = [5, 6, "butas", 58]
end_string = "string"
print(add_string(value=date, end_string=end_string))