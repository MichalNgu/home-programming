import random

def hra_uhodni_cislo():
    cislo = random.randint(1, 100)
    pokusy = 0

    print("Vítej ve hře Uhádni číslo!")
    print("Myslím si číslo mezi 1 a 100.")

    while True:
        hadane_cislo = int(input("Uhádni číslo: "))
        pokusy += 1

        if hadane_cislo < cislo:
            print("Myslím si větší číslo.")
        elif hadane_cislo > cislo:
            print("Myslím si menší číslo.")
        else:
            print(f"Správně! Uhádl jsi číslo {cislo} po {pokusy} pokusech.")
            break

hra_uhodni_cislo()
