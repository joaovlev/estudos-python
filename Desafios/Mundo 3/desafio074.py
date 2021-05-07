from random import randint
lista = []
for c in range(1, 6):
    numero = randint(1, 10)
    lista.append(numero)
print(f'Números sorteados: {lista}')
print(f'O maior número sorteado foi {max(lista)}\nO menor número foi {min(lista)}')
