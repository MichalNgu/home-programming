def prevod_eur_na_czk(castka_eur, kurz):
    """Funkce pro převod eur na CZK."""
    return castka_eur * kurz

def main():
    kurz_eur_czk = 25.5  

    castka_eur = float(input("Zadejte částku v eurech: "))

    castka_czk = prevod_eur_na_czk(castka_eur, kurz_eur_czk)

    print(f"{castka_eur} EUR je {castka_czk} CZK")

if __name__ == "__main__":
    main()
