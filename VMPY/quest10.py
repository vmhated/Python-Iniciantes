from time import sleep
#VARIÁVEIS INICIAIS
alunos = []
idadeglobal = []
notas = []
#VARIÁVEL ESTILO
estilo = '-'*20
#MENUS IMPORTANTES
menu1 = f'''{estilo}
BEM VINDO AO NOSSO SISTEMA,O QUE DESEJA FAZER?
(1)CADASTRAR ALUNO
(2)CONSULTAR ALUNO
(3)SAIR
{estilo}'''
menu2 = f'''{estilo}
DESEJA PERMANECER NESSE SISTEMA?
(4)SIM
(5)NÃO
{estilo}'''
menu3 = f'''{estilo}
O QUE DESEJA FAZER AGORA?
(6)CADASTRAR OUTRO ALUNO
(7)CONSULTAR ALUNO
(8)SAIR
{estilo}'''
#FUNÇÕES ÚTEIS
def receberalunos():
    #FUNÇÃO BASEADA NO MODELO DA FUNÇÃO recebernota() | ln 52-66
    while True:
        try:
            print(f'''{estilo}
BEM VINDO AO CADASTRO DE ALUNOS
{estilo}''')
            alunointerno = input("Digite o nome do aluno:").title().strip()
            if alunointerno.isdigit():
                raise ValueError("Números não são permitidos")
            elif alunointerno in alunos:
                print("ALUNO JÁ CADASTRADO")
                alunointerno = input("CADASTRE OUTRO ALUNO:").title().strip()
                alunos.append(alunointerno)
            else:
                alunos.append(alunointerno)
            break
        except ValueError as e:
            print(e)
def receberidade():
    idadeinterna = int(input("Digite a idade do aluno:"))
    if idadeinterna > 0:
        idadeglobal.append(idadeinterna)
    else:
        print("IDADE INVÁLIDA")
        idadeinterna = int(input("Digite uma idade válida:"))
        idadeglobal.append(idadeinterna)
#FUNÇÃO ABAIXO FEITA POR IA POR MOTIVOS DE BURRICE MAIOR
def recebernota():
    while True:
        try:
            nota = float(input("Digite a nota do aluno (-1 PARA SAIR): "))
            
            if nota == -1:
                break  # Sai do loop se for -1
            
            if 0 <= nota <= 10:
                notas.append(nota)  # Apenas adiciona notas válidas
            else:
                print("❌ NOTA INVÁLIDA! Digite um valor entre 0 e 10.")

        except ValueError:
            print("⚠️ Entrada inválida! Digite um número válido.")
def media(indice):
    return sum(notas) / len(notas)
def consultaralunos():
    while True:
        nomeconsulta = input("Digite o nome do aluno que você deseja consultar:").title().strip()
        try:
            if nomeconsulta.isdigit():
                raise ValueError("Números não são aceitos")
            elif nomeconsulta in alunos:
                print(f"O aluno {nomeconsulta} foi encontrado!")
                print("CARREGANDO INFORMAÇÕES.")
                sleep(1)
                print("CARREGANDO INFORMAÇÕES..")
                sleep(0.5)
                print("CARREGANDO INFORMAÇÕES...")
                #AGRADEÇO AO MEU AMIGO CAIO ROD,POR O CÓDIGO ABAIXO,QUE EU NÃO SABIA COMO FAZER
                index = alunos.index(nomeconsulta)
                print(f"Idade do aluno:{idadeglobal[index]}")
                print(f"Média do aluno:{media(index)}")
                break
        except ValueError as e:
            print(e)  

def sair():
    print("Saindo do sistema...")
    sleep(2)
    print("SISTEMA ENCERRADO,GRATO POR O SEU USO!")
#LOOP PRINCIPAL
print(menu1)
print("OBS:NA PRIMEIRA VEZ DE EXECUÇÃO ESCOLHA SEMPRE 1 OU 3")
opc1 = int(input("Digite a opção desejada:"))
while True:
    match opc1:
        case 1:
            receberalunos()
            receberidade()
            recebernota()
            print(menu2)
            continuarmenu = int(input("Deseja continuar? (4)SIM (5)NÃO:"))
            if continuarmenu == 4:
                continue
            elif continuarmenu == 5:
                print("CADASTRO CONCLUÍDO,SALVANDO ALTERAÇÕES...")
                sleep(2)
                print("...")
                sleep(2)
                print("Alterações salvas")
                sleep(1.5)
                print(menu3)
                opcmenu3 = int(input("O QUE DESEJA FAZER AGORA?(6),(7) OU (8):"))
                if opcmenu3 == 6:
                    continue
                elif opcmenu3 == 7:
                    consultaralunos()
                    print(menu3)
                    opcmenu3 = int(input("O QUE DESEJA FAZER AGORA?(6),(7) OU (8):"))
                    if opcmenu3 == 6:
                        continue
                    elif opcmenu3 == 8:
                        sair()
                        break
                elif opcmenu3 == 8:
                    sair()
                    break
        case 2:
            consultaralunos()
        case 3:
            sair()
            break
#PROGRAMA FINALIZADO EM 18/03/25
'''ESSE FOI O PROJETO MAIS DEMORADO DA MINHA VIDA ATÉ O MOMENTO,GOSTEI MUITO DO DESAFIO DE DESENVOLVER UM SISTEMA DO ZERO
#VISCABARÇA
VMHATED,24-26'''