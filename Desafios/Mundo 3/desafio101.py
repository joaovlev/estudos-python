from datetime import datetime


def voto(ano_nascimento):
    now = datetime.now().year
    idade = now - ano_nascimento
    print(f"Você tem {idade} anos.")
    if idade >= 18:
        return print("VOTO OBRIGATÓRIO!")
    if idade >= 65:
        return print("VOTO OPCIONAL!")
    if idade < 18:
        return print("NAO VOTA!")


usuario = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
voto(usuario)