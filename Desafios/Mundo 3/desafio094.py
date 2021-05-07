from statistics import mean
pessoa = dict()
pessoas = list()
idades = list()
mulheres_cadastradas = list()
while True:
    pessoa.clear()
    pessoa["nome"] = input("Nome: ").strip().title()
    pessoa["idade"] = int(input("Idade: "))
    pessoa["sexo"] = input("Sexo[M/F]: ").strip().upper()[0]
    while pessoa["sexo"] not in ["M", "F"]:
        print("Por favor, digite M ou F.")
        pessoa["sexo"] = input("Sexo[M/F]: ").strip().upper()[0]
    if pessoa["sexo"] == 'F':
        mulheres_cadastradas.append(pessoa["nome"])
    pessoas.append(pessoa.copy())
    idades.append(pessoa["idade"])
    confirmacao = input("Deseja continuar? ").strip().upper()
    while confirmacao not in ["SIM", "S", "NAO", "NÃO", "N"]:
        print("Erro! Digite somente SIM ou NÃO.")
        confirmacao = input("Deseja continuar? ").strip().upper()
    if confirmacao in ["SIM", "S"]:
        continue
    if confirmacao in ["NAO", "NÃO", 'N']:
        break
print(f"Ao todo, {len(pessoas)} pessoas foram cadastradas.")
print(f"A média das idades das pessoas cadastradas é {mean(idades):.2f}.")
print(f"As mulheres cadastradas foram {mulheres_cadastradas}.")
print("Lista de pessoas com idade acima da média: ")
for p in pessoas:
    if p["idade"] > mean(idades):
        print("     ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
print("")
print("<< ENCERRADO >>")