a = int(input("Digite o valor de a: "))
while a == 0:
    a = int(input("Digite um valor diferente de zero para a: "))
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    D = (b**2) - (4 * a * c)
    if D < 0:
        print("Delta negativo. As raízes não são reais.")
    else:
        D = D**0.5
        x1 = (-b + D) / (2 * a)
        x2 = (-b - D) / (2 * a)
        print("Esta é a primeira raiz:", x1)
        print("Esta é a segunda raiz:", x2)
