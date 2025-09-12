senhacorreta = "1234"
nome ="admin"
tentativas = 0
usuario = str(input("digite o nome do usario:"))
while tentativas < 3:
    senha = int(input("digite a sua senha: "))
    if usuario == nome and senha == int(senhacorreta):
        print("acesso permitido")
        break
    else:
        tentativas += 1
        if tentativas < 3:
            print("usuario ou senha incorreta tente novamente")
        else:
            print("acesso negado")
            print("tente novamente mais tarde")
            break