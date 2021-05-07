lista = []
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    lista += [peso]
print(lista)
print('O maior peso foi:', max(lista))
print('O menor peso foi:', min(lista))