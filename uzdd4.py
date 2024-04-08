"""
Sukurkite funkciją, kuri priima eilučių sąrašą ir grąžina naują sąrašą, kuriame yra tik tos eilutės, kurios prasideda balsiu.
"""

def find_words_whit_voices(voices):
    letter = "aouiye"
    text = [text for text in voices if text[0] in letter]
    return text

listas = ["car", "bike", "legs", "airplane"]
print(find_words_whit_voices(listas))


