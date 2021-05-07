from statistics import mean
lista = []
while True:
    n = input('Digite um número: ')
    lista += n
    user = input('Deseja continuar ? (Sim/Não) ').upper()
    if user in ['SIM', 'S']:
        continue
    elif user in ['NÃO', 'N']:
        break
    while True:
        if user not in ['SIM', 'S', 'NÃO', 'N']:
            print('Digite uma opção válida (Sim ou Não).')
            user = input('Deseja continuar ? (Sim/Não) ').upper()
            break
media = mean(lista)
maior = max(lista)
menor = min(lista)
print(f'A média dos números digitados é {media}')
print(f'O maior número digitado foi o número {maior}\ne o menor número digitado foi {menor}')
