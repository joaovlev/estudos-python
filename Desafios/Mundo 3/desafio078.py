valores = []
for c in range(1,6):
    numeros = int(input('Digite um valor -> '))
    valores.append(numeros)
print(f'O maior valor digitado foi o {max(valores)}\nO menor valor digitado foi o {min(valores)}')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'Maior valor nas posições {pos}')
    if valor == min(valores):
        print(f'Menor valor nas posições {pos}')
