from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1, 8):
    nascimento = int(input(f'Em que ano a {pess}ª pessoa nasceu ? '))
    idade = atual - nascimento
    if idade > 18:
        tmaior += 1
    else:
        tmenor += 1
print(f'Ao todo, existem {tmaior} pessoas maiores e {tmenor} pessoas menores.')