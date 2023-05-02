'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Žitník
email: zitnik.david@seznam.cz
discord: DavidŽ#0653
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

# registrovani uzivatele
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# prihlaseni uzivatele
name = input("username:").lower()
password = input("password:")

line = "-" * 40
if name in users and password == users.get(name):
    print(line)
    print("Welcome to the app,", name)
else:
    print("unregistered user, terminating the program..")
    exit()

print("We have 3 texts to be analyzed.")
print(line)
# vyber textu se kterym se bude pracovat
text_number = input("Enter a number btw. 1 and 3 to select:")
print(line)

if text_number.isdecimal():
    if 1 <= int(text_number) <= 3:
        pass
    else:
        print("The value is not within the allowed range.")
        exit()
else:
    print("The value is not a number")
    exit()

# ----- statistika -----
text_list = TEXTS[int(text_number)-1].split()
# pocet slov celkem
words_sum = len(text_list)
# pocet slov zacinajici velkymi pismeny
words_cap_letter = len([word for word in text_list if word[0].isupper()])
# pocet slov velkymi pismen
words_capital = len([word for word in text_list if word.isupper() and word.isalpha()])
# pocet slov velkymi pismeny
words_lower = len([word for word in text_list if word.islower()])
# pocet cisel
numbers_count = len([word for word in text_list if word.isnumeric()])
# soucet cisel v textu
numbers_sum = 0
for word in text_list:
    if word.isnumeric():
        numbers_sum += int(word)

print(f'''There are {words_sum} words in the selected text.
There are {words_cap_letter} titlecase words.
There are {words_capital} uppercase words.
There are {words_lower} lowercase words.
There are {numbers_count} numeric strings.
The sum of all the numbers {numbers_sum}''')

# --- sloupcovy graf ---
# nejdrive se vlozi cely graf do listu, aby se podle nejvetsiho poctu hvezdicek spravne odsadila i hlavicka grafu
graph = []
max_size = 0
for word_lenght in range(1, 12):
    graph_line = [str(word_lenght)]                     # vytvoreni "radku grafu"
    same_lenght = 0
    for word in text_list:
        if word[-1] == "," or word[-1] == ".":          # kontrola posledniho pismene slova (tecky, carky)
            word = word[:-1]
        if word_lenght == len(word):                    # porovnavani delky slova
            same_lenght += 1
            if same_lenght > max_size:
                max_size = same_lenght                  # nejsirsi sloupec grafu
    graph_line.append("*" * same_lenght)                # pridani hvezdicek
    graph.append(graph_line)                            # pridani radku do grafu

print(line)
print(f"LEN|{'OCCURENCES':^{max_size + 2}}|NR.")
print(line)
for raw in graph:
    print(f'{raw[0]:>3}|{raw[1]:<{max_size + 2}}|{len(raw[1])}')
