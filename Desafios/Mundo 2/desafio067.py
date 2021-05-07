from time import sleep
cont = 0
n = int(input('Digite um número para saber sua tabuada: '))
sleep(0.5)
while cont < 10:
    cont += 1
    tabuada = n*cont
    print(f'{n}x{cont} = {tabuada}')
    if n < 0:
        break
