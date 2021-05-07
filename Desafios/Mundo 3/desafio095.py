jogador = dict()
jogadores = list()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    print(f"{'='*30}")
    jogador['nome'] = input('Nome do jogador: ').title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    for p in range(1, partidas+1):
        gols.append(int(input(f"Quantos gols na partida {p}? ")))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    confirmacao = input("Deseja continuar ?").upper()[0]
    while confirmacao not in ["S", "N"]:
        print("Por favor, digite SIM ou NÃO.")
        confirmacao = input("Deseja continuar ?").upper()[0]
    if confirmacao in "S":
        continue
    if confirmacao in "N":
        break
print(f"{'-='*30}")
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print("")
print(f"{'-'*40}")
for k, v in enumerate(jogadores):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print("")
print(f"{'-'*40}")
while True:
    busca = int(input("Qual jogador deseja acessar ? (999 para encerrar) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"Erro! Não existe jogador com código {busca}!")
    else:
        print(f"Levantamento do jogador {jogadores[busca]['nome']}:")
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f"      No jogo {i+1} fez {g} gols")
    print(f"{'-'*40}")
print("<< VOLTE SEMPRE >>")