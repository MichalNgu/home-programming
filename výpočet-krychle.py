def spocti_objem_krychle(delka_strany):
    objem = delka_strany ** 3
    return objem

def spocti_povrch_krychle(delka_strany):
    povrch = 6 * (delka_strany ** 2)
    return povrch

delka_strany = float(input("Zadej délku strany krychle: "))

objem = spocti_objem_krychle(delka_strany)
povrch = spocti_povrch_krychle(delka_strany)

print("Objem krychle je:", objem)
print("Povrch krychle je:", povrch)
