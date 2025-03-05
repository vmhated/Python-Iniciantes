dogname = input("Digite o nome do cachorro:")
comidaquant = int(input("Digite a quantidade de comida que você tem:"))
try:
    comidaquant = -1
    if comidaquant <= 0:
        raise ValueError("quantidade de comida tem que ser maior que zero")
except ValueError as e:
    print(f"O erro é: {e}")