dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Ano de nascimento'] = int(input('Ano de nascimento: '))
dados['Ano de nascimento'] = 2021 - dados['Ano de nascimento']
dados['Idade'] = dados['Ano de nascimento']
del(dados['Ano de nascimento'])
dados['Carteira de trabalho'] = int(input('Carteira de trabalho: '))
if dados['Carteira de trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + 35
for k, v in dados.items():
    print(f"{k} tem valor {v}")