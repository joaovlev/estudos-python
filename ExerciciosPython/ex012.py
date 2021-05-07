#resposta = int(input('Qual a sua idade ? '))
#if resposta == 18:
#   print(18)
#if resposta >= 18:
#    print('+18')
nome_idade = []
while True:
    nome = input('Digite um nome: ').title()
    idade = int(input('Digite uma idade: '))
    nome_idade.append({nome: idade})
    confirmacao = input('Deseja continuar ? [Sim/Não]').upper()
    while confirmacao not in ['S', 'SIM', 'N', 'NAO', 'NÃO']:
        confirmacao = input('Deseja continuar ? [Sim/Não]').upper()
    if confirmacao in ['S', 'SIM']:
        continue
    else:
        break
print(nome_idade)





