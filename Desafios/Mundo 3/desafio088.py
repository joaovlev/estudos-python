from random import randint
from time import sleep
sorteio = list()
jogos = list()
print('-'*30)
print('     JOGA NA MEGA SENA       ')
print('-'*30)
quantidade = int(input('Quantos jogos você deseja jogar ? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(0, 60)
        if numero not in sorteio:
            sorteio.append(numero)
            cont += 1
        if cont >= 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    total += 1
print(f'SORTEANDO {quantidade} JOGOS')
for i, l in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {i+1}: {l}')
print('BOA SORTE!')

