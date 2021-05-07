# Refazendo o exercício 35 do mundo 1 (triângulo)
print('Analisador de Triângulos\n')
r1 = float(input('Digite um segmento: '))
r2 = float(input('Digite outro segmento: '))
r3 = float(input('Digite mais um segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1==r2==r3:
    print('Os segmentos podem formar um triângulo!\n')
    print('O triângulo será equilátero.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 or r2 == r3 or r1 == r3:
    print('Os segmentos podem formar um triângulo!\n')
    print('O triângulo será isósceles.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 != r3:
    print('Os segmentos podem formar um triângulo!\n')
    print('O triângulo será escaleno.')
else:
    print('Seus segmentos não podem formar um triângulo')
