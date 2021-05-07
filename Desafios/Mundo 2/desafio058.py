# Desafio 028 (jogo da adivinhação)
from random import randint
n = randint(1, 10)
print('Pensei em um número entre 0 e 10, tente adivinhar qual número foi')
n_user = int(input('Seu palpite: '))
palpites = 0
while n_user != n:
    print('Você errou o número, tente novamente.')
    n_user = int(input('Seu palpite: '))
    palpites += 1
    if n_user == n:
        print('Parabéns, você acertou')
        print(f'Seus palpites até acertar foram {palpites} palpites.')
        break



