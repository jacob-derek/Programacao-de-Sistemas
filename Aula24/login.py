import customtkinter as tk
from tkinter import messagebox
import sqlite3

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

ph = PasswordHasher()

janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("320x380")

widgets_container = tk.Frame(janela)
widgets_container.place(relx=0.5, rely=0.5, anchor="center")

with sqlite3.connect("senhas.db") as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)


def VerificarLogin():
    usuario = login.get().strip()
    senha_digitada = senha.get()

    if not usuario or not senha_digitada:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    try:
        with sqlite3.connect("senhas.db") as conn:
            resultado = conn.execute(
                "SELECT senha FROM Senhas WHERE login = ?",
                (usuario,)
            ).fetchone()

        if resultado is None:
            messagebox.showerror(
                "Erro",
                "Login ou senha incorretos."
            )
            return

        hash_senha = resultado[0]

        try:
            ph.verify(hash_senha, senha_digitada)

            messagebox.showinfo(
                "Sucesso",
                "Login autorizado."
            )

        except VerifyMismatchError:
            messagebox.showerror(
                "Erro",
                "Login ou senha incorretos."
            )

        except VerificationError:
            messagebox.showerror(
                "Erro",
                "Não foi possível verificar a senha."
            )

    except sqlite3.Error:
        messagebox.showerror(
            "Erro",
            "Não foi possível acessar o banco de dados."
        )


def AdicionarUsuario():
    usuario = login.get().strip()
    senha_nova = senha.get()

    if not usuario or not senha_nova:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    try:
        hash_senha = ph.hash(senha_nova)

        with sqlite3.connect("senhas.db") as conn:
            conn.execute(
                "INSERT INTO Senhas (login, senha) VALUES (?, ?)",
                (usuario, hash_senha)
            )

        messagebox.showinfo(
            "Sucesso",
            "Cadastro concluído."
        )

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Erro",
            "Esse nome de usuário já existe."
        )

    except sqlite3.Error:
        messagebox.showerror(
            "Erro",
            "Não foi possível acessar o banco de dados."
        )


login = tk.Entry(
    widgets_container,
    width=30,
    relief="flat",
    justify="center"
)

senha = tk.Entry(
    widgets_container,
    show="*",
    width=30,
    relief="flat",
    justify="center"
)

entrar = tk.Button(
    widgets_container,
    text="Entrar",
    command=VerificarLogin,
    width=10
)

cadastrar = tk.Button(
    widgets_container,
    text="Cadastrar",
    command=AdicionarUsuario,
    width=10
)

sair = tk.Button(
    widgets_container,
    text="Sair",
    command=janela.destroy,
    width=10,
    bg="#1a1b26",
    fg="#FFFFFF",
    relief="flat",
    justify="center"
)

# Desenhando e atualizando
login.pack(pady=5)
senha.pack(pady=5)
entrar.pack(pady=5)
cadastrar.pack(pady=5)
sair.pack(pady=5)

janela.mainloop()