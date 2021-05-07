salario = float(input('Qual é o seu salário atuaL ? '))
aumento1 = salario + (salario*0.1)
aumento2 = salario + (salario*0.15)
if salario <= 1250.00:
    print(f'Seu aumento será de 15%, seu salário com aumento será: {aumento2}')
else:
    print(f'Seu aumento será de 10%, seu salário com aumento será: {aumento1}')
