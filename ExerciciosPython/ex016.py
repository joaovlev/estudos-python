def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")


soma(6, 3)
soma(4, 8, 6, 2)