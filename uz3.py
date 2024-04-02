"""
Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
"""

def creating_stuff():
   num =  int(input("Enter a nummber: "))
   num1 = int(input("Enter a nummber: "))

   call1 = num + num1
   call2 = num - num1
   call3 = num * num1
   call4 = num / num1
   return  call1, call2, call3, call4

result = creating_stuff()
print("sum", result[0])
print("subtrcation", result[1])
print("multiplication", result[2])
print("division", result[3])




