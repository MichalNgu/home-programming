import time
jmeno = input("Jaké je tvé jméno? ")
print ("Ahoj, " + jmeno, "Čas hrát hangmana!")
time.sleep(1)
print ("Začni hádat...")
time.sleep(0.5)
slovo = ("písmeno", "slovo", "písmena", "slova", "složky")
hady = ''
pokyny = 10
while pokyny > 0:
    chyby = 0
    for pismeno in slovo:
        if pismeno in hady:
            print (pismeno,end=""),
        else:
            print ("_",end=""),
            chyby += 1
    if chyby == 0:
        print ("Vyhrál jsi")
        break
    hadani = input("Hádej písmeno:")
    hady += hadani
    if hadani not in slovo:
        pokyny -= 1
        print ("Špatně")
        print ("Máš", + pokyny, 'pokusů' )
        if pokyny == 0:
            print ("Prohrál jsi")