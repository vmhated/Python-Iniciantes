#Ano Bissexto#
ano= int(input("Digite o ano:"))
if ano/4 or ano/400 and not ano/100:
	print("Ano é bissexto")
else:
	print("Ano é normal")
