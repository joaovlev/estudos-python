numeros = ('zero', 'um','dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
user = int(input('Digite um número entre 0 e 20: '))
for pos, numeros in enumerate(numeros):
    if user > 20:
        user = int(input('Digite um número entre 0 e 20: '))
    if user == pos:
        print(f'O número que você escolheu foi {numeros}')

