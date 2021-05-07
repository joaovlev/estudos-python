n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m} !')
if m < 7:
    print('Você foi reprovado')
else:
    print('Você foi aprovado')