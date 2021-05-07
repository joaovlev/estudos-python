def area(largura, comprimento):
    a = largura * comprimento
    print(f"A aréa de um terreno {largura} x {comprimento} é {a}m²")


print("CONTROLE DE TERRENOS")
print("-" * 30)
l = float(input("LARGURA(m): "))
c = float(input("COMPRIMENTO(m): "))
area(l, c)

