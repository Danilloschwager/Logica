temperatura = float(input("digite a temperatura em celsius: "))
if temperatura > 30:
    print(f"Está a {temperatura} grau celsius,vista roupas leves ")
elif temperatura >= 15:
    print(f"está a {temperatura} grau celsius, vista roupas confortaveis ")
elif temperatura < 15:
    print(f"está a {temperatura} grau celsius, leve um moletom ")
