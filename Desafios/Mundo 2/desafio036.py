print(f"""{'='*20} Empréstimo {'='*20}""")
valor_casa = float(input('Qual o valor da casa que deseja comprar ? '))
salario = float(input('Qual é o seu salario atual? '))
anos = float(input('Em quantos anos você deseja pagar ? '))
meses = anos*12
prestacao = valor_casa/meses
if prestacao > salario*0.30:
    print('Desculpe, porém você não atende os requisitos para o empréstimo')
else:
    print(f"Sua prestação será de R$ {prestacao} ao mês por {meses} meses")