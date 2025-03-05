
def nota_para_passar_de_ano(nome_do_aluno, nota_do_aluno, nota_media=6, nota_maxima=10):

    if nota_do_aluno == nota_maxima:
        print(f'{nome_do_aluno} conseguiu nota máxima')
    elif nota_do_aluno >= nota_media and nota_do_aluno != nota_maxima:
        print(f"{nome_do_aluno} Aprovado por pouco")
    else:
        print(f'{nome_do_aluno} Reprovado :(') 
nome_do_aluno = input("Digite o nome do aluno:")
nota_do_aluno = float(input("Digite a nota do aluno:"))
class aluno:
    def __init__(self,nome_do_aluno,nota_do_aluno):
        self.nomealuno = nome_do_aluno
        self.nota = nota_do_aluno
    def condicoes(self):
        return nota_para_passar_de_ano(self.nomealuno, self.nota, nota_media=6, nota_maxima=10)

aluno1 = aluno(nome_do_aluno,nota_do_aluno)
print(aluno1.condicoes())
