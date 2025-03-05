import random
numalet = random.randint(1, 10)
numuser = int(input("Digite um número de 1 a 10:"))
while numuser != numalet:
   numuser2 = int(input("Digite um número de 1 a 10:"))
   if numuser2 == numalet:
      print("Você acertou!")
      break