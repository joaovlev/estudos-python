temp = list()
dados = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    temp.append(media)
    dados.append(temp[:])
    temp.clear()
    confirmacao = input('Deseja continuar ?').upper()
    if confirmacao in ['SIM', 'S']:
        continue
    if confirmacao in ['NÃO', 'NAO', 'N']:
        break
print('No. NOME      MÉDIA')
for pos, p in enumerate(dados):
    print(''*1, pos+1, ''*4, p[0], ' '*5, p[3])
print(dados)
while True:
    acessar_nota = int(input('Deseja acessar as notas de qual aluno ? (Aperte 999 para finalizar) '))
    if acessar_nota == 999:
        print('Finalizado.')
        break
    if acessar_nota <= len(dados) - 1:
        print(f'Notas de {dados[acessar_nota][0]} são {dados[acessar_nota][1], dados[acessar_nota][2]}')






