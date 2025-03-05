import random
dogname = input("Digite o nome do cachorro:")
comidaquant = int(input("Digite a quantidade de comida que você tem:"))
class Cachorro:
    def __init__(self,dogname,comidaquant):
        self.nome = dogname
        self.food = comidaquant
    def comer(self):
            dogcomer = random.randint(1,comidaquant)
            self.food = comidaquant - dogcomer
            print(f"O cachorro {self.nome} comeu: {dogcomer} comidas de {comidaquant},sobraram {self.food}")
dog1 = Cachorro(dogname,comidaquant)
dog1.comer()
dog2 = Cachorro(dogname = input("Digite o nome do cachorro 2:"),comidaquant = int(input("Digite a quantidade de comida do cachorro 2:")))
dog2.comer()