#VARIÁVEIS INICIAS
frutas = []
cor = []
#ESTILO
estilo = "-"*20
#MENUS
menufruta = f'''{estilo}
DIGITE O NOME DA FRUTA PARA ASSOCIAR A COR
{estilo}'''
menucor = f'''{estilo}
DIGITE A COR PARA ASSOCIAR COM A FRUTA
{estilo}'''
#FUNÇÕES
def addfruta():
    print(menufruta)
    while True:
        frutainterna = input("Digite o nome da fruta:").title().strip()
        try:
            if frutainterna.isdigit():
                raise ValueError("Digite apenas letras")
            else:
                frutas.append(frutainterna)
        except ValueError as e:
            print(e)
        print('''DESEJA CONTINUAR A ADD FRUTAS?
(S)SIM
(N)NÃO''')
        opcfruta = input("Digite uma opção:").strip().upper()
        if opcfruta == "S":
            continue
        elif opcfruta == "N":
            break
def addcor():
    print(menucor)
    while True:
        corinterna = input("Digite a cor da fruta:").title().strip()
        try:
            if corinterna.isdigit():
                raise ValueError("Digite apenas letras")
            else:
                cor.append(corinterna)
        except ValueError as e:
            print(e)
        print('''DESEJA CONTINUAR A ADD CORES?
(S)SIM
(N)NÃO''')
        opccor = input("Digite uma opção:").strip().upper()
        if opccor == "S":
            continue
        elif opccor == "N":
            break
def consultafruta():
    while True:
        frutaconsulta = input("Digite o nome da fruta para consultar a cor:").title().strip()
        index = frutas.index(frutaconsulta)
        if frutaconsulta in frutas:
            print(f"A fruta {frutaconsulta} tem a cor {cor[index]}")
        elif frutaconsulta not in frutas:
            print("Fruta não encontrada")
            addfruta()
            addcor()
        print(f'''{estilo}
DESEJA CONSULTAR OUTRA FRUTA?
(S)SIM
(N)NÃO
{estilo}''')
        opcconsulta = input("Digite uma opção:").strip().upper()
        if opcconsulta == "S":
            continue
        elif opcconsulta == "N":
            print(f"{estilo}SISTEMA ENCERRADO,GRATO POR SEU USO{estilo}")
            break
#CÓDIGO PRINCIPAL
addfruta()
addcor()
consultafruta()
#PROGRAMA FEITO POR MIM SEM AJUDA DE INTELIGÊNCIA ARTIFICIAL
#13:53 | 19/03/2025
#vmhated,24-26
