from random import choice
print('Jokenpô')
jokenpo = input('Jogue jokenpô com o programa: ').upper()
programa = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print(f'Programa: {programa}')
if programa == 'PEDRA' and jokenpo == 'TESOURA':
    print('O programa ganhou!')
elif programa == 'PAPEL' and jokenpo == 'PEDRA':
    print('O programa ganhou!')
elif programa == 'TESOURA' and jokenpo == 'PAPEL':
    print('O programa ganhou!')
elif programa == jokenpo:
    print('Houve um empate!')
else:
    print('Parabéns, você ganhou do programa!')