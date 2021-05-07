primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(primeiro_termo, 21, razao):
    print(c, '->', end= ' ')
print('ACABOU!')
