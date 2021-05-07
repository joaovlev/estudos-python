print(f"""
{'='*24}
Sequência de fibonacci
{'='*24}
""")
n = int(input('Digite um número para saber sua sequência: '))
t1 = 0
t2 = 1
contador = 3
while contador <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    contador += 1
    print(f'{t1} -> {t2} -> {t3}', end='')
print(' -> Fim')
