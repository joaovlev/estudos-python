lista = list()
valores_digitados = 0
valor_5 = 0
while True:
    numero = int(input('Digite um número: '))
    valores_digitados += 1
    lista.append(numero)
    lista.sort(reverse=True)
    confirmacao = input('Deseja continuar ? [Sim/Não]').upper()
    if confirmacao in ['SIM', 'S']:
        continue
    if confirmacao in ['NÃO', 'NAO', 'N']:
        print(f'{valores_digitados} valores foram digitados.')
        print(f'Lista com os valores decrescentes: {lista}')
        if 5 in lista:
            print('O número 5 foi digitado!')
        else:
            print('O valor 5 não foi digitado!')
        break
