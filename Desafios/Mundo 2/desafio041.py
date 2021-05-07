print(f"\033[31m{'='*20} Conferência de natação {'='*20}\033\n")
ano_de_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2021 - ano_de_nascimento
print(f'Você tem {idade} anos.')
if idade <= 9:
    print('Categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria SÊNIOR')
elif idade > 20:
    print('Categoria Master')


