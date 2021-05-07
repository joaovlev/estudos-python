total = 0
produto_1000 = 0
menor = 0
contador = 0
barato = ''
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Preço: R$ '))
    contador += 1
    total += preco
    confirmacao = input('Deseja comprar mais produtos?(Sim/Não) ').strip().upper()
    if contador == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if preco > 1000:
        produto_1000 += 1
    while confirmacao not in ['S', 'SIM', 'N','NÃO', 'NAO']:
        confirmacao = input('Deseja comprar mais produtos?(Sim/Não) ').strip().upper()
    if confirmacao in ['N', 'NÃO', 'NAO']:
        break
print(f'O total a pagar pelos produtos será R${total}')
print(f'{produto_1000} produtos custam mais que mil reais.')
print(f'O produto mais barato foi {barato} que custa R${menor}')



