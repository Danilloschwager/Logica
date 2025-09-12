nota1 = float(input("digite sua primerira nota: "))
nota2 = float(input("digite sua segunda nota: "))
media = (nota1 + nota2) /2
print(F"sua media é {media}: ")

if media >= 7:
    print("você passou de ano !")
elif media >= 5:
    print("você está de recuperação")
else:
    print("você está reprovado!")
    

