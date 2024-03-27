"""
Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys. Reikšmę galite saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas, kol rasite tą, kurią įvedėte.
"""
import random

password = str(random.randint(0000, 9999)).zfill(4)
answer = int()
print("Generate", password)

while True:
    answer = str(random.randint(0000, 9999)).zfill(4)
    if password == answer:
        print(answer)
        break
    else:
        print("Still looking :", answer)