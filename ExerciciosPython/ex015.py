pessoas = []
dados = []
total_maiores = 0
total_menores = 0
for c in range(0,5):
    dados.append(input('Nome: ').title())
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for p in pessoas:
    if p[1] >= 21:
        total_maiores += 1
        print(f'{p[0]} é maior de idade')
    else:
        total_menores += 1
        print(f'{p[0]} é menor de idade')
print(f'Existem {total_maiores} maiores de idade')
print(f'Existem {total_menores} menores de idade')