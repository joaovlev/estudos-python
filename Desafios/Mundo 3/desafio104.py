def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        global n
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[31mERRO! digite apenas números inteiros.\033[m")
        if ok:
            break
    return valor


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")