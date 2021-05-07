frase = str(input('Digite uma frase: ')).lower().strip()
quantidade = frase.count('a')
print(f"Sua frase tem {quantidade} a's")
print('Posição do primeiro a: ', frase.find('a')+1)
print('Posição do último a: ', frase.rfind('a')+1)

