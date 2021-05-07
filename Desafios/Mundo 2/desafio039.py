ano_de_nascimento = int(input('Qual o ano do seu nascimento? '))
idade = 2021 - ano_de_nascimento
print(f'Você tem {idade} anos!')
tempo_restante = 18 - idade
tempo_excedido = idade - 18
if idade == 18:
    print('Você deverá se alistar esse ano!')
elif idade > 18:
    print('Você já deveria ter se alistado!')
    print(f'Você excedeu o tempo de alistamento em: {tempo_excedido} ano(s)!')
elif idade < 18:
    print(f'Tempo restante até o alistamento: {tempo_restante} anos!')
