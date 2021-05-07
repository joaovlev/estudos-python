from random import randint
valores_sorteados = list()
pares_sorteados = list()


def sorteio():
    for c in range(0, 5):
        valores_sorteados.append(randint(1, 10))
    print(f"Os valores sorteados foram {valores_sorteados}")


def soma(lista):
    for v in valores_sorteados:
        if v % 2 == 0:
            pares_sorteados.append(v)
    print(f"Os pares sorteados foram {pares_sorteados} e a soma deles é {sum(pares_sorteados)}")


sorteio()
soma(valores_sorteados)
