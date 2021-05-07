valores = list()
while True:
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        valores.sort()
        print('Valor adicioando!')
    else:
        print('Valor descartado. (duplicado)')
    confirmacao = input('Deseja continuar ? [S/N]').upper()
    if confirmacao in ['SIM', 'S']:
        continue
    if confirmacao in ['NÃO', 'NAO', 'N']:
        print(f'Os valores digitados são: {valores}')
        break



