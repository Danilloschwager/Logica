def jogo_tabela_verdade():
    print("\nBem-vindo à Simulação Virtual da Lógica!")
    print("Você é um agente digital tentando escapar de um sistema de segurança baseado em lógica.")
    print("Para se libertar, precisa quebrar os 6 códigos lógicos que protegem o núcleo do sistema!")
    input("Pressione Enter para iniciar a simulação...")

    pontos = 0
    desafios = [
        {
            'historia': "Nível 1: Você acessa o primeiro firewall lógico.",''
            'pergunta': 'Se A é verdadeiro e B é falso, A ∨ B é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'a'
        },
        {
            'historia': "Nível 2: Um antivírus tenta te detectar com uma verificação booleana.",
            'pergunta': 'Se A é falso, então ¬A é?',
            'opcoes': ['a) False', 'b) True'],
            'resposta': 'b'
        },
        {
            'historia': "Nível 3: Um labirinto lógico aparece com armadilhas baseadas em conectivos.",
            'pergunta': 'Se A é verdadeiro e B é verdadeiro, A ∧ B é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'a'
        },
        {
            'historia': "Nível 4: Você chega a uma sala espelhada onde a lógica se inverte.",
            'pergunta': 'Se A é falso e B é verdadeiro, A → B é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'a'
        },
        {
            'historia': "Nível 5: Uma IA tenta te confundir com uma afirmação contraditória.",
            'pergunta': 'Se A é verdadeiro e B é falso, A ↔ B é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'b'
        },
        {
            'historia': "Nível 6: No núcleo do sistema, o Enigma Final te desafia.",
            'pergunta': 'Se A é falso e B é falso, A ∨ B é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'b'
        }
    ]

    for i, desafio in enumerate(desafios):
        print(f"\n{desafio['historia']}")
        print(f"Desafio {i+1}: {desafio['pergunta']}")
        for opcao in desafio['opcoes']:
            print(opcao)
        resposta = input("Sua resposta (a/b): ").strip().lower()
        if resposta == desafio['resposta']:
            print("Correto! Você quebrou mais uma camada do sistema.")
            pontos += 1
        else:
            print("Errado! Um alarme dispara, mas você continua tentando.")
        if i == 2:
            print("\nVocê encontra um script oculto: 'A verdade sempre encontra um caminho.'")
        if i == 4:
            print("\nUma mensagem codificada aparece: 'Nem tudo que parece falso é inválido.'")

    print(f"\nSimulação encerrada! Você acertou {pontos} de {len(desafios)} desafios.")
    if pontos == len(desafios):
        print("Parabéns! Você dominou a lógica e escapou do sistema com maestria!")
    else:
        print("Você sobreviveu, mas ainda há bits de lógica a decifrar. Continue praticando!")

# Para jogar, descomente a linha abaixo:
jogo_tabela_verdade()
