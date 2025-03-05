sinais = ["+","-","*","/"]
while True:
    operacao = input("digite sua operação:")
    while operacao not in sinais:
        operacao = input("Digite uma operação existente:")
    n1 = int(input("Digite o number 1:"))
    n2 = int(input("Digite o number 2:"))
    match operacao:
        case "+":
            print(f"A soma de {n1} e {n2} é igual a:{n1+n2}")
        case "-":
            print(f"A subtração de {n1} e {n2} é igual a: {n1-n2}")
        case "":
            print(f"A multi de {n1} e {n2} é igual a:{n1*n2}")
        case "/":
            if n2 == 0:
                break
            else:
                print(f"A divisão de {n1} por {n2} é igual a:{n1/n2}")