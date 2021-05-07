quantidades_de_9 = 0
lista_numeros_total = []
lista_numeros_pares = []
for c in range(1, 5):
    num = int(input('Digite um número: '))
    lista_numeros_total.append(num)
    if 9 in lista_numeros_total:
        quantidades_de_9 += 1
    if num % 2 == 0:
        lista_numeros_pares.append(num)
if 3 not in lista_numeros_total:
    print('O valor 3 não foi digitado')
else:
    print(f'O primeiro número três foi digitado primeiramente posição {lista_numeros_total.index(3)}')
print(f'O número 9 apareceu {quantidades_de_9} vezes.')
print(f'Os números pares digitados foram: {lista_numeros_pares}')
