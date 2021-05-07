from time import sleep
soma = 0
numeros = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    sleep(0.5)
    numeros += 1
    soma += n
print(f'Você digitou {numeros} números.')
print(f'A soma dos números é {soma}.')