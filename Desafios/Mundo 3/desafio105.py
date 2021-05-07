from statistics import mean
lista_notas = list()
dados = dict()


def notas(lista_das_notas):
    while True:
        nota = float(input("Nota: "))
        lista_notas.append(nota)
        confirmacao = input("Deseja continuar ?").upper()[0]
        if confirmacao == 'S':
            continue
        if confirmacao == 'N':
            dados['quantidade de notas'] = len(lista_notas)
            dados['maior nota'] = max(lista_notas)
            dados['menor nota'] = min(lista_notas)
            dados['media'] = mean(lista_notas)
            if mean(lista_notas) < 7:
                dados['situação'] = "Turma reprovada"
            else:
                dados['situação'] = "Turma aprovada"
            break
    print(dados)


notas()
