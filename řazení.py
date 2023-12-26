def serad_slova(text):
    seznam_slov = text.split()
    serazena_slova = sorted(seznam_slov)
    serazeny_text = ' '.join(serazena_slova)
    return serazeny_text

slova = "pes kočka ryba had"
vysledek = serad_slova(slova)
print(f"Seřazená slova: {vysledek}")
