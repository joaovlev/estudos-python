lista = []
lista_pares = []
lista_impares = []
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    confirmacao = input('Deseja continuar ? ').upper()
    if confirmacao in ['SIM', 'S']:
        continue
    if confirmacao in ['NÃO', 'NAO', 'N']:
        print(f'Lista com os valores: {lista}')
        print(f'Lista com os valores pares digitados: {lista_pares}')
        print(f'Lista com os valores ímpares digitados: {lista_impares}')
        break

