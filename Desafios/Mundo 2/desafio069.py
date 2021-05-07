print('Cadastrando dados\n')
maiores = 0
homens = 0
mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '.upper()
    while sexo not in ['M', 'F']:
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
        if idade >= 18:
            maiores += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres20 += 1
        elif idade >= 18:
            maiores += 1
    resp = ' '
    while resp not in ['S', 'SIM', 'N', 'NAO', 'NÃO']:
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp in ['N', 'NÃO', 'NAO']:
        break
print(f'Há {maiores} maiores de 18 anos cadastrados.')
print(f'Há {homens} homens cadastrados.')
print(f'Há {mulheres20} mulheres com menos de 20 anos cadastradas.')



