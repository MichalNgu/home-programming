def vypocet_dph(castka_bez_dph, sazba_dph):
    dph = castka_bez_dph * (sazba_dph / 100)
    
    castka_s_dph = castka_bez_dph + dph
    
    return castka_s_dph, dph

castka_bez_dph = float(input("Zadejte částku bez DPH: "))
sazba_dph = float(input("Zadejte sazbu DPH (%): "))

castka_s_dph, dph = vypocet_dph(castka_bez_dph, sazba_dph)

print(f"Celková částka s DPH: {castka_s_dph:.2f} Kč")
print(f"DPH: {dph:.2f} Kč")