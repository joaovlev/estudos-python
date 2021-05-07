from time import sleep


def contador(inicio, fim, passo):
    print("-="*20)
    print(f"Contando de {inicio} até {fim} de {passo} em {passo}")

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            sleep(0.5)
            print(f"{cont} ", end="")
            cont += passo
        print("<< FIM >>")
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(f"{cont} ", end="")
            cont -= passo
        print("<< FIM >>")


print("----------- CONTADOR -----------")
contador(1, 10, 1)
contador(10, 0, 2)
print("----------- SUA VEZ -----------")
i = int(input("INÍCIO: "))
f = int(input("FIM: "))
p = int(input("PASSO: "))
contador(i, f, p)

