n = int(input('Digite um número: '))
total_divisores = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        total_divisores += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {total_divisores} vezes')
if total_divisores == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')
