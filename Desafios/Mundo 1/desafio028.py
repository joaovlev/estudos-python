from random import randint
n1 = randint(0, 5)
print('Pensei em um número de 0 a 5, tente adivinhar qual foi!')
resposta = int(input('Digite aqui: '))
if resposta == n1:
    print('Parabéns, você acertou o número!')
else:
    print('Você errou, tente novamente.')
print(f'O número que pensei foi: {n1}')
print('Sua chance de acertar é de 20%')