"""c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')"""
"""r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Quer continuar ? (S/N) ').upper()
print('fim')"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você dgitou {par} números pares')
print(f'Você dgitou {impar} números ímpares')

