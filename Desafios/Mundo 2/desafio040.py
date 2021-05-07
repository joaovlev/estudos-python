nota1 = float(input('Digite sua nota em Português: '))
nota2 = float(input('Digite sua nota em Matemática: '))
nota3 = float(input('Digite sua nota em História: '))
nota4 = float(input('Digite sua nota em Geografia: '))
nota5 = float(input('Digite sua nota em Ciências: '))
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
print('Sua média precisa ser acima de 7 para que você seja aprovado.')
print(f'Sua média foi: {media}')
if media < 5.0:
    print('Você foi reprovado!')
elif media > 5.0 and media < 7.0:
    print('Você está em recuperação!')
elif media > 7:
    print('Você foi aprovado!')
