preço = float(input("digite o preço da primerira loja: "))
preço2 = float(input("digite o preço da segunda loja: "))
if preço > preço2:
    print(f"A primeira loja está cobrando {preço} ela está mais cara")
elif preço2 > preço:
    print(f"A segunda loja está cobrando {preço2} ela está mais cara")
else:
    print("Ambas estão no mesmo preço")




