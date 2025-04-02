print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Maryna Kulhánková
email: marie.paskova@seznam.cz
""")


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

cara = "-" * 40
print(cara)

registered_users = {
    "bob": "123",
    "mike": "password123",
    "liz": "pass123",
    "ann": "pass123",
}

username = input("username: ")
password = input("password: ")

if username in registered_users and registered_users[username] == password:
    print(f"""Welcome to the app {username},
    We have 3 texts to be analyzed.
    """)
else:
    print("Your username or password is incorrect!")
    print("Unregistered user, terminating the program..")
    exit()


def analyze_text(text):
    words = text.split()
    num_words = len(words)
    num_capitalized = sum(1 for word in words if word[0].isupper())
    num_uppercase = sum(1 for word in words if word.isupper())
    num_lowercase = sum(1 for word in words if word.islower())
    num_numbers = sum(1 for word in words if word.isdigit())
    sum_numbers = sum(int(word) for word in words if word.isdigit())

    print(f"\nThere are {num_words} words in the selected text.")
    print(f"There are {num_capitalized} titlecase words.")
    print(f"There are {num_uppercase} uppercase words.")
    print(f"There are {num_lowercase} lowercase words.")
    print(f"There are {num_numbers} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers}")


choice = input("Enter a number btw. 1 and 3 to select: ")

if choice.isdigit():
    choice = int(choice)
    if 1 <= choice <= 3:
        selected_text = TEXTS[choice - 1]
        analyze_text(selected_text)
    else:
        print("Invalid number. Exiting.")
else:
    print("Invalid input. Exiting.")

print(cara)


length_counts = {}

for text in TEXTS:
    words = text.split()
    for word in words:
        length = len(word)
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1


print(f"{'LEN':<4}| {'OCCURRENCES':<36}| {'NR.':>3}")
print(cara)
for length in sorted(length_counts.keys()):
    count = length_counts[length]
    stars = "*" * count
    print(f"{length:<4}| {stars:<36}| {count:>3}")

