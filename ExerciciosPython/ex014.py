valores = []
for c in range(1, 11):
    numeros = int(input('Digite um valor: '))
    valores.append(numeros)
for pos, valor in enumerate(valores):
    print(f'Na posição {pos} eu encontrei o valor {valor}.')
# Adicionar cópia de uma lista.
a = [2, 5, 6, 8]
b = a[:] # Recebeu uma cópia dos valores de A

