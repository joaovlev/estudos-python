sexo = input('Digite seu sexo: ').upper()
while sexo not in ['M', 'F']:
    print('Por favor, digite um valor válido (M ou F).')
    sexo = input('Digite seu sexo: ').upper()
    if sexo in ['M', 'F']:
        break


