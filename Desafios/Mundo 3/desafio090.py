dados = {'nome': '', 'media': '', 'situacao': ''}
dados['nome'] = input('Nome: ')
dados['media'] = float(input(f"Média de {dados['nome']} : "))
if dados['media'] > 7:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'
print(f"Nome é igual a {dados['nome']}")
print(f"Média é igual a {dados['media']}")
print(f"Situação é igual a {dados['situacao']}")