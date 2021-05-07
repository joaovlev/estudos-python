print(f"""
{'='*27}
Olá, seja bem vindo a loja!
{'='*27}
""")
produto_valor = float(input('Qual o valor do produto que você deseja ? '))
print("""
Selecione sua forma de pagamento:

(1) Dinheiro/Cheque
(2) Cartão de crédito
""")
forma = input('').upper()
if forma in ['1', 'DINHEIRO', 'CHEQUE']:
    print('Você terá 10% de desconto com esta forma de pagamento!')
    print(f'O valor a pagar será de {produto_valor - (produto_valor*0.10)}')
elif forma in ['2', 'CARTÃO', 'CARTÃO DE CRÉDITO']:
    print("""
    Selecione o número de parcelas:
    (1) Á vista
    (2) 2x sem juros
    (3) 3x com 20% de juros 
    """)
    forma_cartao = input('').upper()
    if forma_cartao in ['1', 'Á VISTA']:
        print('Você terá 5% de desconto nesta forma de pagamento.')
        print(f'O valor total a pagar será {produto_valor - (produto_valor*0.05)} R$.')
    elif forma_cartao in ['2', '2x']:
        print(f'O valor total a pagar será 2x de {produto_valor/2}')
    elif forma_cartao in ['3', '3x']:
        parcelas = produto_valor/3
        juros = parcelas + parcelas*0.20
        print('Você terá um juros de 20% com esta forma de pagamento.')
        print(f'O valor total a pagar será 3x de {juros} R$')