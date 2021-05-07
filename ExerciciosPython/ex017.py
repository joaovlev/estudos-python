def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Par ou Impar: "))
if par(num):
    print("PAR")
else:
    print("IMPAR")