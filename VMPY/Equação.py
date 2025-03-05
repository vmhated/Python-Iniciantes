a = int(input("Digite o a:"))
while a == 0:
    a = int(input("Digite outro valor para a:"))
b = int(input("Digite o b:"))
c = int(input("Digite o c:"))
D = ((b**2) - 4 * a * c)**0.5
if D > 0:
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    print(f"O valor de X1 é:{x1}")
    print(f"O valor de X2 é:{x2}")
else:
    print("Não exite raiz real")

