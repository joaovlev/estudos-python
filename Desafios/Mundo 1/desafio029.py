velocidade = float(input('Qual a sua velocidade atual: '))
print('O limite de velocidade é 80Km/h')
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('Você está dentro do limite, Dirija com cuidado!')
else:
    print('Você está acima da velocidade e será multado!')
    print(f'Valor da multa = R${multa}')
