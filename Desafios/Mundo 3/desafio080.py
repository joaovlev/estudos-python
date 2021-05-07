valores = list()
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {valores}')
