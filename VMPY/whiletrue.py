sinais = ["+","-","*","/"]
while True:
    operacao = input("digite sua operação:")
    while operacao not in sinais:
        operacao = input("Digite uma operação existente:")
    n1 = float(input("Digite o number 1:"))
    n2 = float(input("Digite o number 2:"))
    match operacao:
        case "+":
            print(f"A soma de {n1} e {n2} é igual a:{n1+n2}")
        case "-":
            print(f"A subtração de {n1} e {n2} é igual a: {n1-n2}")
        case "*":
            print(f"A multi de {n1} e {n2} é igual a:{n1*n2}")
        case "/":
            if n2 == 0:
                print("Divisão por zero é inválida")
                n2 = float(input("Digite um valor diferente de zero:))
            else:
                print(f"A divisão de {n1} por {n2} é igual a:{n1/n2}")
