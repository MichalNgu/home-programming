import math

def spocitej_obsah_obvod_kruhu(polomer):
    obvod = 2 * math.pi * polomer
    obsah = math.pi * (polomer ** 2)
    return obvod, obsah

polomer = float(input("Zadej poloměr kruhu: "))

obvod, obsah = spocitej_obsah_obvod_kruhu(polomer)

print("Obvod kruhu je:", obvod)
print("Obsah kruhu je:", obsah)
