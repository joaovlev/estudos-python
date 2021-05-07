# Refazendo o desafio 51 (Progressão aritmética)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1
while contador <= 10:
    termo += razão
    contador += 1
    print(termo, end=' -> ')
contador = 1
while True:
    resposta = int(input('\nQuantos termos você quer mostrar a mais ? '))
    if resposta == 0:
        break
    while contador <= resposta:
        termo += razão
        contador += 1
        print(termo, end=' -> ')

print('fim')
