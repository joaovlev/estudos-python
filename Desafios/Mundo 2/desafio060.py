from math import factorial
print(f"""
{'=-'*12}
Cauculadora de fatorial
{'=-'*12}
""")
n = int(input('Digite o valor para ser calculado: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')
