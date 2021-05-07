from random import randint
print(f"""
{'='*17}
JOGO PAR OU IMPAR
{'='*17}
""")
vitorias = 0
while True:
    user = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar ? (P/I) ').upper()
    bot = randint(1, 10)
    total = user + bot
    if escolha == 'P' and total % 2 == 0:
        print(f'Você jogou {user} e o bot jogou {bot}. A soma deu {total} e é par')
        print("""
Parabéns, você ganhou!
vamos jogar novamente...
        """)
        vitorias += 1
    elif escolha == 'I' and total % 2 != 0:
        print(f'Você jogou {user} e o bot jogou {bot}. A soma deu {total} e é ímpar')
        print("""
Parabéns, você ganhou!
vamos jogar novamente...
                """)
        vitorias += 1
    elif escolha == 'I' and total % 2 == 0:
        print(f'Você jogou {user} e o bot jogou {bot}. A soma deu {total} e é ímpar')
        print('Você perdeu!')
        break
    elif escolha == 'P' and total % 2 != 0:
        print(f'Você jogou {user} e o bot jogou {bot}. A soma deu {total} e é ímpar')
        print('Você perdeu!')
        break

print(f'\nVocê ganhou {vitorias} vezes.')






