"""
Exercise 1:	Write a Python program to find the most common elements and their counts in a specified text.
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]
"""

def counting_common_elements(text, number=3):
    holder = []
    for l in set(text):
        holder.append((l, text.count(l)))
        holder.sort(key=lambda x: x[1], reverse=True)
    return holder[:3]



text = "lkseropewdssafsdfafkpwe"
print(counting_common_elements(text))


"""
Exercise 2: Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
"""

l1 = [3, 6, 5, 12, 8, 18, 15]
l2 = [3, 1, 12, 16, 6, 24, 4]
result = []

odd = l1[1::2]
even = l2[0::2]

result.extend(odd)
result.extend(even)

print(result)


def picking_odd_even(f: list, s: list) ->list:
        return (f[1::2] + s[::2])

l1 = [3, 6, 5, 12, 8, 18, 15]
l2 = [3, 1, 12, 16, 6, 24, 4]


print(picking_odd_even(f=l1, s=l2))


"""
Exercise 3: Create a Python set such that it shows the element from both lists in a
"""

def return_zipped_data(listas_1, listas_2):
    result = []
    for i in range(len(listas_1)):
        result.append((listas_1[i], listas_2[i]))
    return result

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print(return_zipped_data(listas_1=first_list, listas_2=second_list))


"""
Exercise 4: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
Given:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Expected Outcome:

After removing unwanted elements from list [47, 69, 76, 97]
"""

def removing_same_elements(rolls, samples):
    result = []
    for x in rolls:
        if x in samples.values(): result.append(x)
    return result



roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print(removing_same_elements(rolls=roll_number, samples=sample_dict))

"""
Exercise 5: Get all values from the dictionary and add them to a list but don’t add duplicates
Given:
 
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
Expected Outcome:
 
[47, 52, 44, 53, 54]
"""

def adding_values(dicts):
    sets = set()
    for x in dicts.values():
        if x not in dicts:
            sets.add(x)
    return sets



speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 56, 'Aug': 44, 'Sept': 54}

print(adding_values(dicts=speed))