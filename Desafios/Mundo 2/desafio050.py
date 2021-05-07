soma = 0
for _ in [1, 2, 3, 4, 5, 6]:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print(soma)
