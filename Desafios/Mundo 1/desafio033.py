n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
lista = [n1, n2, n3]
#max(lista)
#min(lista)
lista.sort()
print(f'O maior número é: {lista[-1]}')
print(f'O menor número é: {lista[0]}')
