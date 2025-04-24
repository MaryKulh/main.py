print("""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Maryna Kulhánková
email: marie.paskova@seznam.cz
""")

import random

cara = "-" * 40

def uvod():
    print(cara)
    print("Hi there!")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(cara)

def generuj_tajne_cislo():
    cisla = list("123456789")
    nahodne = random.sample(cisla, 4)
    return "".join(nahodne)

def validuj_vstup(vstup):
    if not vstup.isdigit() or len(vstup) != 4:
        return False
    if len(set(vstup)) != 4:
        return False
    if vstup[0] == "0":
        return False
    return True

def vyhodnot_hadani(hadane, tajne):
    bulls = sum(1 for x, y in zip(hadane, tajne) if x == y)
    cows = sum(1 for x in hadane if x in tajne) - bulls
    return bulls, cows

def main():
    uvod()
    tajne_cislo = generuj_tajne_cislo()
    pokusy = 0
    while True:
        print(cara)
        hadane_cislo = input("Enter a number:\n>>> ")
        print(cara)
        if not validuj_vstup(hadane_cislo):
            print("Invalid input, try again.")
            continue
        pokusy += 1
        bulls, cows = vyhodnot_hadani(hadane_cislo, tajne_cislo)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        if bulls == 4:
            print(cara)
            print(f"Correct, you've guessed the right number\nin {pokusy} guesses!")
            print(cara)
            print("That's amazing!")
            break

if __name__ == "__main__":
    main()

