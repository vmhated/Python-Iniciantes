number = int(input("Insira um número:"))
op = input("Digite a operção(+,-,x ou /):")
cont = 0
for cont in range(-1,9):
    cont += 1
    if op == "x":
        print(f"{number} {op} {cont} = {number*cont}")
    elif op == "+":
        print(f"{number} {op} {cont} = {number+cont}")
    elif op == "-":
        cont += 1
        print(f"{number} {op} {cont} = {number - cont}")
    elif op == "/":
        cont += 1
        print(f"{number} {op} {cont} = {number / cont}")
    else:
        print("Operador inválido")