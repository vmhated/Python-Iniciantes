escolha = ""
pedido = []

print("\nEscolha as opções para seu sanduiche.")
print("Selecione os ingrediente pelo número do menu.")
print("Ao concluir, digite 0 para fechar o pedido.\n")

while True:
    print('''
    1-Pão de Forma
    2-Pão Árabe
    3-Carne
    4-Peru
    5-Ovo
    6-Bacon
    7-Alface
    8-Cebola
    9-Tomate
    0-Fechar pedido''')
        
    escolha = input("Adicionar item: ")
    class escolha:
        match escolha:
         case "1":
            pedido.append("Pão de Forma")
            print(pedido)
         case "2":
            pedido.append("Pão Árabe")
         case "3":
            pedido.append("Carne")
         case "4":
            pedido.append("Peru")
         case "5":
            pedido.append("Ovo")
         case "6":
            pedido.append("Bacon")
         case "7":
            pedido.append("Alface")
         case "8":
            pedido.append("Cebola")
         case "9":
            pedido.append("Tomate")
         case "0":
            break
         case _:
            print("Opção inválida!")
print(f'''Seu sanduíche ficou: {"".join(pedido)}
      Obrigado pela preferência!''')
