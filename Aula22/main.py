import sqlite3
from prompt_toolkit import radiolist_dialog

#tenho que conectar e criar um cursor

conexao = sqlite3.connect("curso.db")
cursor = conexao.cursor()

#####       criar a tabela         ####
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
)
""")

conexao.commit()

# tenho que criar variaveis que recebem nome, idade e curso e 
# enfiar isso no sql usando execute(INSERT INTO (blablabla) values (???), (blablabla)
# tudo dentro de parenteses pq to escrevendo bglh

def CriarAluno():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    
    cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?,?,?)", (nome, idade, curso))

    # commit
    conexao.commit()
    print("Aluno adicionado.")



# listar alunos usando fetchall()
def ListarAlunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    for aluno in alunos():
        print(aluno)


opcao = radiolist_dialog(
    title="SQL",
    text="O que deseja fazer?",
    values=[
        ("Adicionar", "Adicionar aluno"),
        ("Listar", "Listar alunos"),
        ("Excluir", "Remover aluno"),
        ("Sair", "Sair"),
    ],
).run()

print("Opcao escolhida: ", opcao)