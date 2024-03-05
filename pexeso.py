import random

def vygeneruj_karty(pocet_karet):
    cisla = list(range(pocet_karet)) * 2
    random.shuffle(cisla)
    return cisla

def hra_pexeso(pocet_karet):
    karty = vygeneruj_karty(pocet_karet)
    karty_otocene = ["X"] * len(karty)
    pocet_pokusu = 0
    nalezeno_paru = 0
    
    print("Vítej ve hře Pexeso!")
    print("Otoč karty a najdi všechny páry.")

    while True:
        print(" ".join(map(str, karty_otocene)))
        if "X" not in karty_otocene:
            print("Gratulujeme, našel/a jsi všechny páry!")
            break
        
        volba1 = int(input("Vyber první kartu (zadej číslo od 0 do {}): ".format(len(karty) - 1)))
        volba2 = int(input("Vyber druhou kartu (zadej číslo od 0 do {}): ".format(len(karty) - 1)))

        if volba1 == volba2 or volba1 < 0 or volba1 >= len(karty) or volba2 < 0 or volba2 >= len(karty):
            print("Neplatná volba. Zkus to znovu.")
            continue

        if karty[volba1] == karty[volba2]:
            print("Gratulujeme, našel/a jsi pár!")
            karty_otocene[volba1] = karty[volba1]
            karty_otocene[volba2] = karty[volba2]
            nalezeno_paru += 1
        else:
            print("Špatně! Zkus to znovu.")
        
        pocet_pokusu += 1

    print("Počet pokusů:", pocet_pokusu)

# Spuštění hry s 8 kartami (4 páry)
hra_pexeso(4)