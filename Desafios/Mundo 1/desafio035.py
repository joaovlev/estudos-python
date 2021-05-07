print('-'*30)
print('Analisador de Triângulos')
print('-'*30)
r1 = float(input('Digite um segmento: '))
r2 = float(input('Digite outro segmento: '))
r3 = float(input('Digite mais um segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Seus segmentos não podem formar um triângulo')
