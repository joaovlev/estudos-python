from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = n1 + n2
multiplicacao = n1*n2
user = 0
while user != '5':
    print("""
    O que você deseja ?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Digitar novos valores
    [5] Sair
        """)
    user = input('Digite uma das opções: ')
    if user == '1':
        print(f'A soma dos valores é: {soma}')
    elif user == '2':
        print(f'O produto dos valores é {multiplicacao}')
    elif user == '3':
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif user == '4':
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))






