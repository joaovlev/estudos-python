peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso/altura**2
print(f'Seu IMC (Índice de massa corporal) é {IMC}')
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif IMC > 18.5 and IMC <= 25:
    print('Você está com um peso ideal.')
elif IMC > 25 and IMC <= 30:
    print('Você está com sobrepeso.')
elif IMC > 30 and IMC <= 40:
    print('Você está com obesidade')
elif IMC > 40:
    print('Você está com obesidade mórbida')