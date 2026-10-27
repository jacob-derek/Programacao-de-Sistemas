import sqlite3                    # importar a biblioteca do sql

conn = sqlite3.connect("filmes.db")    # puxar o banco, se nao existir ele cria automaticamente
cursor = conn.cursor()                # criar um cursor pra passar comandos sql pro banco

try:
    # SQL é lingagem de comandos.
    # na atividade proposta precisa dos 5 seguintes:
        # CREATE TABLE - criar uma tabela
        # INSERT INTO - adicionar linhas
        # SELECT - ler as linhas existentes
        # UPDATE - alterar linhas
        # DELETE - para remover linhas
    
    # e tem os tipos - TEXT, INTEGER e REAL
    
    #######################################################
    # para criar uma tabela:
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            ano INTEGER,
            genero TEXT,
            duracao_min INTEGER,
            nota REAL
        )
    """)
    
    #################################
    # MODELO:
    # nome da tabela
    # coluna - linha, tipo e condicao
    #################################
    
    #######################################################
    # inserindo dados - ? é o placeholder pras variaveis a serem inseridas
    
    # cursor.execute(
    #    "INSERT INTO Filmes (titulo, ano, genero, duracao_min, nota) VALUES (?,?,?,?,?)", 
    #    ("Interestelar", 2014, "Ficção Científica", 169, 8.7)
    #)
    
    # para inserir varios de uma vez é so usar uma lista de tuplas e inserir no placeholder
    # IMPORTANTE: use, tambem, cursor.executemany(flags)
    
    filmes = [
    ("Detachment", 2011, "Drama", 100, 3.0),
    ("Whiplash", 2014, "Drama", 106, 8.5),
    ("Em Ritmo de Fuga", 2017, "Ação", 113, 7.5),
    ("Rocky, Um Lutador", 1976, "Drama", 119, 8.1),
    ("Psicopata Americano", 2000, "Suspense", 101, 7.6),
    ]
    
    cursor.executemany(
        "INSERT INTO Filmes (titulo, ano, genero, duracao_min, nota) VALUES (?,?,?,?,?)", 
        filmes
    )
    conn.commit() # salvar tudo lá
    
    #######################################################
    # agora vamos mostrar os filmes anexados à tabela
    ########### READ ###########
    print("\n--- Todos os Filmes ---")
    cursor.execute("SELECT * FROM Filmes")
    for filme in cursor.fetchall():
        print(filme)
    
    # para filtrar, use WHERE
    # cursor.execute('SELECT * FROM Filmes WHERE coluna > ?', (ITEM DE ACORDO COM O TIPO DA LINHA DESSS COLUNA,))
    # conn.commit()

    print("\n--- Filmes com nota acima de 7.0 ---")
    cursor.execute('SELECT * FROM Filmes WHERE nota >= ?', (7.0,))
    for filme in cursor.fetchall():
        print(filme)
    
    # para atualizar, use UPDATE:
    # cursor.execute('UPDATE Filmes SET coluna = ? WHERE id = ?', (ITEM DE ACORDO '',))
    # conn.commit()

    ########### ATUALIZANDO A NOTA DE DETACHMENT  ###########
    cursor.execute('UPDATE Filmes SET nota = ? WHERE ID = ?', (9.0, 1))
    conn.commit()
    
    ########### MOSTRANDO OQ ATUALIZEI ###########
    cursor.execute('SELECT * FROM Filmes WHERE id = ?', (1,))
    print(cursor.fetchone())
    
    # para deletar, use DELETE
    # cursor.execute('DELETE FROM Filmes coluna = ? WHERE id = ?', (ITEM DE ACORDO '',))
    # conn.commit()
    
    print("\n            ADICIONANDO E APAGANDO NOVO FILME:")
    filme_qualquer = "A Casa de Cera"
    cursor.execute(
        "INSERT INTO Filmes (titulo, ano, genero, duracao_min, nota) VALUES (?,?,?,?,?)", 
        (filme_qualquer, 2005, "Terror", 113, 5.5)
    )
    cursor.commit()
    
    print("\n            Mostrando oq adicionei:")
    cursor.execute('SELECT * FROM Filmes WHERE titulo = ?', (filme_qualquer,))
    for filme in cursor.fetchall():
        print(filme)
    
    print("\n            Apagando esse filme bosta:")
    cursor.execute('DELETE FROM FILMES WHERE titulo = ?', (filme_qualquer,))
    cursor.commit()
    
    print("\n-----------------------------------------------")
    print("\n--- CATALOGO FINAL ---")
    cursor.execute('SELECT * FROM Filmes')
    for filme in cursor.fetchall():
        print(filme)

except sqlite3.Error as erro:
    print("Erro no banco: ", erro)
finally:
    conn.close()