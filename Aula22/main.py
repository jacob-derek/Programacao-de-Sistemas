import sqlite3
from prompt_toolkit.shortcuts import radiolist_dialog

#tenho que conectar e criar um cursor

conexao = sqlite3.connect("curso.db")
cursor = conexao.cursor()

#####       criar a tabela         ####

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER,
        curso TEXT
    )
    """)
    
    conexao.commit()
except sqlite3.Error as error:
    printf(f"Erro: {error}")

# tenho que criar variaveis que recebem nome, idade e curso e 
# enfiar isso no sql usando execute(INSERT INTO (blablabla) values (???), (blablabla)
# tudo dentro de parenteses pq to escrevendo bglh

def CriarAluno():
    nome = input("Nome: ").strip()
    if not nome:
        print("Preencha corretamente.")
        return
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Preencha corretamente com numeros inteiros.")
        return

    curso = input("Curso: ").strip()

    try:
        cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?,?,?)", (nome, idade, curso))
        conexao.commit()
        print("Aluno adicionado.")
    except sqlite3.Error as error:
        conexao.rollback(f"{error}")
        print("")


def ExcluirAluno():
    id_aluno = int(input("ID do aluno: "))
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))

    conexao.commit()
    print("Deletado.")


# listar alunos usando fetchall()
def ListarAlunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    if alunos != 0:
        for aluno in alunos:
            print(aluno)
    else:
        print("Nenhum aluno registrado.")


acoes = {
    "Adicionar": CriarAluno,
    "Listar": ListarAlunos, 
    "Excluir": ExcluirAluno
}

while True:
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

    if opcao is None or opcao == "Sair":
        pass

    acao = acoes.get(opcao)
    if acao:
        acao()

    cursor.close()
    conexao.close()