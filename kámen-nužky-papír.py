import random

def hra_kamen_nuzky_papir():
    moznosti = ["kámen", "nůžky", "papír"]
    
    while True:
        volba_hrace = input("Zvolte kámen, nůžky nebo papír: ").lower()
        if volba_hrace not in moznosti:
            print("Neplatná volba. Zkuste to znovu.")
            continue
        
        volba_pocitace = random.choice(moznosti)
        
        print("Počítač zvolil:", volba_pocitace)
       
        if volba_hrace == volba_pocitace:
            print("Remíza!")
        elif (volba_hrace == "kámen" and volba_pocitace == "nůžky") or \
             (volba_hrace == "nůžky" and volba_pocitace == "papír") or \
             (volba_hrace == "papír" and volba_pocitace == "kámen"):
            print("Gratulujeme! Vyhráváte!")
        else:
            print("Bohužel, prohráli jste.")
        
        opakovani = input("Chcete hrát znovu? (ano/ne): ").lower()
        if opakovani != "ano":
            break

hra_kamen_nuzky_papir()