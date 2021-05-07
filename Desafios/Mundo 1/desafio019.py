from random import choice
aluno1 = input('Escreva o nome dos alunos: ')
aluno2 = input('Escreva o nome dos alunos: ')
aluno3 = input('Escreva o nome dos alunos: ')
aluno4 = input('Escreva o nome dos alunos: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print(f'O aluno que irá apagar o quadro é o número: {sorteio}')
