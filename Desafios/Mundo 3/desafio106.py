class Carro:
    def __init__(self, marca, ano, origem):
        self.marca = marca
        self.ano = ano
        self.origem = origem


    def exibir(self):
        return print(f"""
        A marca do carro é {self.marca}
        O ano do carro é {self.ano}
        A origem do carro é {self.origem}
        """)


    def abrirportas(self):
       return print("As portas estão abertas")


    def fecharportas(self):
        return print("As portas estão fechadas")


    def trocarpneus(self):
        return print("Os pneus estão trocados")

marca_usuario = input("Digite a marca do carro: ")
ano_carro = int(input("Digite o ano do carro: "))
origem_carro = input("Digite a origem do carro: ")
carro1 = Carro(marca_usuario, ano_carro, origem_carro)
print(f"{carro1.marca, carro1.origem, carro1.ano}")
