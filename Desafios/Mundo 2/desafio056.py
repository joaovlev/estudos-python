soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulheres_20 = 0
for p in range(1, 5):
    pessoa = print(f"""{'-'*5} {p}ª pessoa {'-'*5} """)
    nome = str(input(f'Qual é o nome da {p}ª pessoa? \n')).title()
    idade = int(input(f'Qual é a idade da {p}ª pessoa? \n'))
    sexo = str(input(f'Qual é o sexo da {p}ª pessoa (M/F)? \n')).upper()
    soma_idade += idade
    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome
    elif sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        total_mulheres_20 += 1
media_idade = soma_idade / 4
print(f'A media das idades das 4 pessoas é: {media_idade}')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {total_mulheres_20} mulheres menores de 20 anos!')