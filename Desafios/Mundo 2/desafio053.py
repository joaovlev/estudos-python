print(f"""\033[31;1m
{'=-'*15}
Detector de palíndromo
{'=-'*15}
\033[m""")
frase = str(input('Digite uma frase: '))
frase_formatada = frase.replace(' ', '')
frase_upper = frase.upper()
inverso = ''
for letra in range(len(frase_upper)-1, -1, -1):
    inverso += frase_upper[letra]
print(f'A frase junta é {frase_upper}')
print(f'A frase invertida é {inverso}')
if frase_upper == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')

