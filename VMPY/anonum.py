#Ano Bissexto#
ano= int(input("Digite o ano:"))
if ano/4 or ano/400 and not ano/100:
	print("Ano é bissexto")
else:
	print("Ano é normal")
#Positivo,negativo ou zero#
N1 = int(input("Digite o número:"))
if N1>0:
	print("Número é positivo")
elif N1<0:
	print("Número é negativo")
else:
	print("Número é zero")
	
