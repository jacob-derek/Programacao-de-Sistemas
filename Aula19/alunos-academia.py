#dicionario com alunos e dias q foram pra academia
#a recepcao digita o nome do ultimo aluno a entrar
#se o nome ja estiver no sistema, contar +1 dia e deixar passar
#tratar exception

banco_academia = {
"nomes" : [],
"frequencia" : []

}

def Recepcao():
    def AdicionarAluno(nome_aluno):
        banco_academia["nomes"].append(nome_aluno)
    
    
    while True:
        recep_option = int(input("""Que operação realizar?
    1 - Adicionar Aluno
    2 - Listar alunos
    3 - Sair\n"""))
        
        
        if recep_option == 3:
            break
        elif recep_option == 2:
            for aluno in banco_academia["nomes"]:
                print(aluno)
        elif recep_option == 1:
            recep_nome_param = input("Qual o nome do aluno?: ")
            AdicionarAluno(recep_nome_param)

Recepcao()
