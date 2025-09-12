def jogo_tabela_verdade():
    print("\nBem-vindo ao mundo da Lógica!")
    print("Você é um aventureiro em busca de um  Cristal da Verdade.")
    print("Para avançar, precisa resolver os problemas de tabela verdade em 6 níveis de desafios!")
    input("Pressione Enter para começar sua jornada...")

    pontos = 0
    desafios = [
        {
            'historia': "Nível 1: Você chega à Ponte do Pensamento, guardada por um velho sábio.",
            'pergunta': 'Se P é verdadeiro e Q é falso, P ∧ Q é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'b'
        },
        {
            'historia': "Nível 2: Após atravessar a ponte, você encontra uma porta mágica com um enigma.",
            'pergunta': 'Se P é verdadeiro, então ¬P é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'b'
        },
        {
            'historia': "Nível 3: Um dragão de lógica bloqueia seu caminho e só deixará você passar se resolver seu desafio.",
            'pergunta': 'Se P é falso e Q é verdadeiro, P ∧ Q é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'b'
        },
        {
            'historia': "Nível 4: Você encontra uma bruxa que lança um feitiço de confusão lógica!",
            'pergunta': 'Se P é verdadeiro e Q é verdadeiro, P ↔ Q é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'a'
        },
        {
            'historia': "Nível 5: No Salão das perguntas ih respostas...",
            'pergunta': 'Se P é falso e Q é falso, P → Q é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'a'
        },
        {
            'historia': "Nível 6: Finalmente, diante do Cristal da Verdade, o grande sábio final surge!",
            'pergunta': '"Se P é falso e Q é verdadeiro, P ∨ Q é?',
            'opcoes': ['a) True', 'b) False'],
            'resposta': 'a'
        }
    ]

    for i, desafio in enumerate(desafios):
        print(f"\n{desafio['historia']}")
        print(f"Desafio {i+1}: {desafio['pergunta']}")
        for opcao in desafio['opcoes']:
            print(opcao)
        resposta = input("Sua resposta (a/b): ").strip().lower()
        if resposta == desafio['resposta']:
            print("Correto! Você avança na sua jornada.")
            pontos += 1
        else:
            print("Errado! Você caiu, mas continua na jornada.")
        if i == 2:
            print("\nVocê encontra uma poção de sabedoria e sente-se mais confiante!")
        if i == 4:
            print("\nVocê ouve uma voz misteriosa: 'A lógica é a chave para todos os portais.'")

    print(f"\nFim da aventura! Você acertou {pontos} de {len(desafios)} desafios.")
    if pontos == len(desafios):
        print("Parabéns! Você conquistou o Cristal da Verdade e se tornou um mestre da lógica!")
    else:
        print("Continue treinando para dominar a lógica e vencer todos os desafios!")

# Para jogar, descomente a linha abaixo:
jogo_tabela_verdade()
 