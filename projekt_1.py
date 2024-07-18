"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Lucie Černochová
email: cernochova.lucie@email.cz
discord: Lucie Č. (lucie.c123)
"""
import math

'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


#regist uživatel - slovník
registr_users = {
            "bob": "123",
            "ann": "pass123",
            "mike": "password123",
            "liz": "pass123" 
            }

line = 50 * "-"

# Vyžádám si od uživatele přihlašovací jméno a heslo.
name_input = input("Username: ")
password = str(input("Password: "))
name = name_input.lower()

print(line)

# Zjistím, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
if name in registr_users and registr_users[name] == password:
# Pokud je uživatel registrovaný, pozdravím jej a umožním mu analyzovat texty.  
    print(f"Welcome to the app, {name.title()}.\nWe have 3 texts to be analyzed.") 
else:
# Pokud uživatel není registrovaný, upozorním ho a ukončím program.
    print("Unregistered user, terminating the program..")
    exit()
    
print(line) 
   
# Vyžádám si od uživatele číslo textu, které chce analyzovat.  
number = input("Enter a number btw. 1 and 3 to select: ")

print(line)

# Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
if not number.isdigit():
    print("The entered value does not contain a number. Terminating the program..")
    exit()
# Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí.
else:
    number = int(number) - 1
    if number not in range(3):
        print("The selected number is not specified in the entry. Terminating the program..")
        exit()
        
select_text = TEXTS[number]      
words = select_text.split()
# Program spočítá, kolik slov je v textu.
word_count = len(words)
print(f"There are {word_count} words in the selected text.")

# Pomocné proměnné
word_count_title = 0
word_count_upper = 0
word_count_lower = 0
word_number = 0
suma_numbers = 0

# Program spočítá počet slov začínajících velkým písmenem.
for word in words:
    if word.istitle():
        word_count_title += 1
# Program spočítá počet slov psaných velkými písmeny.
    elif word.isupper():
        word_count_upper += 1
# Program spočítá počet slov psaných malými písmeny.
    elif word.islower():
        word_count_lower += 1
# Program spočítá počet čísel.        
    elif word.isnumeric():
        word_number += 1
# Program spočítá sumu všech čísel v textu.
        suma_numbers += int(word)
       
# Vypsání podmínek pro jednotlivé výpočty.
print(f"There are {word_count_title} titlecase words.")  
print(f"There are {word_count_upper} uppercase words.")
print(f"There are {word_count_lower} uppercase words.")
print(f"There are {word_number} numeric strings.")
print(f"The sum of all the numbers {suma_numbers}.")

# GRAF ČETNOSTI DÉLEK SLOV.
print(line)
print("LEN|    OCCURRENCES   |NR.")
print(line)

# Slovník pro četnost délek slov.
length_of_words = {}

# Přidání jednotlivých délek slov do slovníku.
for word in words:
    length = len(word)
    if length in length_of_words:
        length_of_words[length] += 1
    else:
        length_of_words[length] = 1
        
# Graf délek slov / výskyt = počet slov se stejnou délkou.
for length, frequency in sorted(length_of_words.items()):
    print(f"{length:<3}| {'*' * frequency:<17}|{frequency}")

   

