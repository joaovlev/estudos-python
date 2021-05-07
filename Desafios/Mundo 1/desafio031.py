distancia = float(input('Qual é a distância da sua viagem em Km ? '))
passagem1 = distancia*0.50
passagem2 = distancia*0.45
if distancia <= 200:
    print('Distância de até 200Km será R$0,50 por Km')
    print(f'O valor da passagem é: R${passagem1}')
else:
    print('Distância para além de 200Km será R$0,45 por Km')
    print(f'O valor da passagem é: R${passagem2}')
