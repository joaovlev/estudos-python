numeros_pares = list()
numeros_impares = list()
lista_final = list()
for c in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
        numeros_pares.sort()
    else:
        numeros_impares.append(numero)
        numeros_impares.sort()
lista_final.append(numeros_pares[:])
lista_final.append(numeros_impares[:])
print(f'A lista com números pares e ímpares é {lista_final}')
