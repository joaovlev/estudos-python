from datetime import datetime
now = datetime.now()
hora = now.hour
minuto = now.minute
segundo = now.second

print('============================== sistema de provas ==============================\n')
print('Bem vindo ao sistema automatizado de provas, agora são', now.strftime('%a'), now.strftime('%b'), now.day,
      f'{hora}:{minuto}:{segundo}', now.year, '\n')
print('===============================================================================\n')
print('Selecione uma prova\n Matematica -> [1]\n Estatística -> [2]\n Física -> [3]\n')
prova = input('Digite a prova que deseja fazer: \n').lower()


if prova == 'matemática' or prova == 'matematica' or prova == '1' or prova == 'm':

    acertos_math = int(0)

    print("""
    Questão 1: Qual o valor de π(PI)
        A) 3,1415926
        B) 3,015
        C) 2,1545132
        D) Nenhuma das alternativas
        """)

    resposta_math_1 = input('').upper()
    while resposta_math_1 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D).')
        resposta_math_1 = input('').upper()
        if resposta_math_1 == 'A':
            acertos_math += 1
        elif resposta_math_1 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 2: Qual o numero de kaprekar 
        A) 6174 e 495 
        B) 6175 e 495
        C) 5000 e 2000
        D) Nenhuma das alternativas.
        """)

    resposta_math_2 = input('').upper()
    while resposta_math_2 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_math_2 = input('').upper()
        if resposta_math_2 == 'A':
            acertos_math += 1
        elif resposta_math_2 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 3: log9  é igual a 
        A) 0.95424250943
        B) 9
        C) 0.8751
        D) Nenhuma das alternativas.
        """)

    resposta_math_3 = input('').upper()
    while resposta_math_3 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_math_3 = input('').upper()
        if resposta_math_3 == 'A':
            acertos_math += 1
        elif resposta_math_3 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 4: Modulo de -5 é igual a 
        A) 5
        B) 10
        C) 15
        D) -5
        """)

    resposta_math_4 = input('').upper()
    while resposta_math_4 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_math_4 = input('').upper()
        if resposta_math_4 == 'A':
            acertos_math += 1
        elif resposta_math_4 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 5: 1 + 2 e igual a
        A) -3
        B) log3
        C) [3]
        D) 5+123+341-653-12341-19827+12357
        """)

    resposta_math_5 = input('').upper()
    while resposta_math_5 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_math_5 = input('').upper()
        if resposta_math_5 == 'C':
            acertos_math += 1
        elif resposta_math_5 in ['A', 'B', 'C', 'D']:
            break

    if acertos_math > 2:
        print('Você foi aprovado em Matemática!')
    else:
        print('Você foi reprovado em Matemática!')
    print(f'Você acertou um total de {acertos_math} questões.')


if prova == 'estatística' or prova == 'estatistica' or prova == '2' or prova == 'e':

    acertos_statistic = int(0)
    print("""
    Questão 1: O que é moda?
        A) Estilo de roupa.
        B) O valor mais frequente de um conjunto de dados.
        C) Media
        D) Moda representa a ordem matemática dos dados.
            """)

    resposta_statistic_1 = input('').upper()
    while resposta_statistic_1 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_statistic_1 = input('').upper()
        if resposta_statistic_1 == 'B':
            acertos_statistic += 1
        elif resposta_statistic_1 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 2: O que é mediana.
        A) Nenhuma das alternativas abaixo.
        B) E quando alguém pede para ana medir algo, mediana
        C) Representa a media
        D) Representa o valor central de um conjunto de dados.
            """)

    resposta_statistic_2 = input('').upper()
    while resposta_statistic_2 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_statistic_2 = input('').upper()
        if resposta_statistic_2 == 'D':
            acertos_statistic += 1
        elif resposta_statistic_2 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 3: Qual a mediana de 18, 19, 19, 22, 44, 45, 46, 46, 47, 48
        A) 45.5
        B) 44.5
        C) 35.4
        D) Nenhuma das alternativas.
            """)
    resposta_statistic_3 = input('').upper()
    while resposta_statistic_3 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_statistic_3 = input('').upper()
        if resposta_statistic_3 == 'A':
            acertos_statistic += 1
        elif resposta_statistic_3 in ['A', 'B', 'C', 'D']:
            break
    print("""
    Questão 4: Qual a  media de 18, 19, 19, 22, 44, 45, 46, 46, 47, 48
        A) 35.4
        B) 35
        C) 30
        D) 36)
            """)

    resposta_statistic_4 = input('').upper()
    while resposta_statistic_4 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_statistic_4 = input('').upper()
        if resposta_statistic_4 == 'A':
            acertos_statistic += 1
        elif resposta_statistic_4 in ['A', 'B', 'C', 'D']:
            break

    print("""Questão 5: O que é media
        A) Representa a soma de de todos os elemementos e a divisao pelo numero total dos elementos.
        B) Representa a soma de de todos os elemementos e a divisao pela metade do total dos elementos.
        C) Representa a soma de de todos os elemementos e a divisao pelo numero total dos elementos.
        D) Representa a soma de de todos os elemementos e a divisao por 2.
        """)

    resposta_statistic_5 = input('').upper()
    while resposta_statistic_5 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_statistic_5 = input('').upper()
        if resposta_statistic_5 == 'C':
            acertos_statistic += 1
        elif resposta_statistic_5 in ['A', 'B', 'C', 'D']:
            break

    if acertos_statistic > 2:
        print('Você foi aprovado em estatística!')
    else:
        print('Você foi reprovado em estatística!')
    print(f'Você acertou um total de {acertos_statistic} questões.')


if prova == 'física' or prova == 'fisica' or prova == '3' or prova == 'f':
    acertos_physics = int(0)
    print("""
    Questão 1: Qual a formula para converter C para F
        A) (°C × 9/5) + 32 
        B) (4 °C × 5/5) + 50 
        C) (4 °C × 7*5) 
        D) (4 °C) + 30
        """)

    resposta_physics_1 = input('').upper()
    while resposta_physics_1 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_physics_1 = input('').upper()
        if resposta_physics_1 == 'A':
            acertos_physics += 1
        elif resposta_physics_1 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 2: qual a formula para converter f para k
        A) (°F − 32) × 5/9 + 273,15
        B) (°F − 32) × 5/9 + 275,15
        C) (°F − 32) × 5/9 + 243,15
        D) (°F − 32) × 5/9 + 223,15
        """)

    resposta_physics_2 = input('').upper()
    while resposta_physics_2 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_physics_2 = input('').upper()
        if resposta_physics_2 == 'A':
            acertos_physics += 1
        elif resposta_physics_2 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 3: 10 Watt corresponde a quantos jaules
        A) 10j
        B) 20j
        C) 30j
        D) Nenhuma das alternativas.
        """)

    resposta_physics_3 = input('').upper()
    while resposta_physics_3 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_physics_3 = input('').upper()
        if resposta_physics_3 == 'A':
            acertos_physics += 1
        elif resposta_physics_3 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 4: Qual a formula para converter k para c
        A) k - 273,15
        B) k - 272,15
        C) k - 223,15
        D) k - 263,15
        """)

    resposta_physics_4 = input('').upper()
    while resposta_physics_4 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_physics_4 = input('').upper()
        if resposta_physics_4 == 'A':
            acertos_physics += 1
        elif resposta_physics_4 in ['A', 'B', 'C', 'D']:
            break

    print("""
    Questão 5: O que é dilatacao linear
        A) A dilatação linear, que é um aumento de comprimento.
        B) A dilatacao linear é quando algo dilata linearmente.
        C) A dilatacao linear é uma dilatacao a frente
        D) A dilatacao linear é linear
        """)

    resposta_physics_5 = input('').upper()
    while resposta_physics_5 not in ['A', 'B', 'C', 'D']:
        print('Por favor, digite uma resposta válida (A, B, C ou D)')
        resposta_physics_5 = input('').upper()
        if resposta_physics_5 == 'A':
            acertos_physics += 1
        elif resposta_physics_5 in ['A', 'B', 'C', 'D']:
            break

    if acertos_physics > 2:
        print('Você foi aprovado em física.')
    else:
        print('Você foi reprovado em física')
    print(f'Você acertou um total de: {acertos_physics} questões.')