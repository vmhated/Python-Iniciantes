#EXEMPLO DE USO 1
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
def apresentar(self):
    print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
apresentar(pessoa(nome,idade))
#EXEMPLO DE USO 2
carro_ = input("Digite o modelo do carro:")
marca = input("Digite a marca do carro:")
ano = input("Digite o ano do carro:")
class carro:
    def __init__(self,carro,marca,ano):
        self.carro = carro
        self.marca = marca
        self.ano = ano
def mostrar(self):
    print(f"Meu carro é:{self.carro},da marca:{self.marca} do ano de:{self.ano}")
mostrar(carro(carro_,marca,ano))
