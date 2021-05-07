dias = int(input('Por quantos dias seu carro foi alugado ? '))
km = int(input('Quantos Km foram rodados ? '))
diasres = dias*60
kmres = km*0.15
total = kmres + diasres
print(f'O total a pagar é: R${total}')