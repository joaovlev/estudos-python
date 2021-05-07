valores = list()

def maior(list):
    print("-="*25)
    print("ANALISANDO OS VALORES")
    print(f"{list} foram informados {len(list)} valores ao todo.")
    print(f"o maior valor informado foi {max(list)}")


usuario = int(input("Quantos valores deseja adicionar a lista ? "))
while len(valores) != usuario:
    valores.append(int(input(f"Valor: ")))
maior(valores)


