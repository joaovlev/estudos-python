def ficha(nome, gols):
    if nome == '':
        nome = "DESCONHECIDO"
    if gols == '':
        gols = '0'
    print(f"O jogador {nome} fez {gols} no campeonato.")


n = input("Nome do jogador: ")
g = input("Quantidade de gols: ")
ficha(n, g)