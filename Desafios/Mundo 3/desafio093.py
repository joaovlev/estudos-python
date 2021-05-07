from operator import itemgetter
dados = dict()
gols = list()
dados['Nome'] = input('Nome do jogador: ')
partidas = int(input('Quantas partidas ele jogou ? '))
for p in range(1, partidas+1):
    gols.append(int(input(f"Quantos gols na partida {p}? ")))
dados['Gols'] = gols
dados['Total'] = sum(gols)
print(f"{'-='*30}")
print(dados)
print(f"{'-='*30}")
for k, v in dados.items():
    print(f"O campo {k} tem valor {v}")
print(f"{'-='*30}")
print(f"O jogador {dados['Nome']} jogou {len(dados['Gols'])} partidas.")
print(f"Foi um total de {dados['Total']} gols")
print(f"{'-='*30}")
for i, v in enumerate(dados['Gols']):
    print(f"Na partida {i+1}, fez {v} gols.")
print(f"{'-='*30}")