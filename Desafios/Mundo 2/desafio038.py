n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O maior número é: {n1}!')
    print(f'O menor número é: {n2}!')
elif n1 < n2:
    print(f'O maior número é: {n2}!')
    print(f'O menor número é: {n1}!')
elif n1 == n2:
    print('Os números são iguais.')