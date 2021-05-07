temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    confirmacao = input('Deseja continuar ?').upper()
    if confirmacao in ['SIM', 'S']:
        continue
    if confirmacao in ['NÃO', 'NAO', 'N']:
        break
print(f'Os dados foram {princ}')
print(f'O total de pessoas cadastradas foram {len(princ)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}], ', end='')