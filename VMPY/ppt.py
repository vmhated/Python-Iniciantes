import random
def jogar():
    user = input("'p' para pedra,'p2'para papel,'t' para tesoura:")
    pc =  random.choice(['p','p2','t'])
    print(f"Pc escolheu:{pc}")
    if user == pc:
        return "Empate" 
    else:
        return victory(user,pc)
    
# p > t,t > p2,p2 > p  
def victory(user,pc):
    if user == "p" and pc == "t" or user == "t" and pc == "p2" or user == "p2" and pc == "p":
        return "Você ganhou!!!"
    else:
        return "Perdeu pra máquina!!!"
def main():
    resultado = jogar()
    print(resultado)
if __name__ == "__main__":
    main()