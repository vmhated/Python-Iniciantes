valor_compra = float(input("Digite o valor da compra:"))
if valor_compra > 200:
    print("Você recebeu 20% de desconto")
    print ("O valor final ficou de:",valor_compra - ((20/100)*valor_compra))
elif valor_compra > 100 and valor_compra < 200:
    print("Você recebeu 10% de desconto")
    print ("O valor final ficou de:",valor_compra - ((10/100)*valor_compra))
elif valor_compra > 0 and valor_compra < 100:
    print("Você recebeu 5% de desconto")
    print ("O valor final ficou de:",valor_compra - ((5/100)*valor_compra))
else:
    print("O produto é 0 reais ou vc digitou um número negativo")
    
