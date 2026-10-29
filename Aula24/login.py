import tkinter as tk
import sqlite3

janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("320x380")

widgets_container = tk.Frame(janela)
widgets_container.place(relx=0.5, rely=0.5, anchor="center")

login = tk.Entry(widgets_container, 
    width=30,
    relief="flat",
    justify="center")

senha = tk.Entry(widgets_container, 
    show="*", 
    width=30,
    relief="flat",
    justify="center")

sair = tk.Button(widgets_container,
    text="Sair", 
    command=lambda: janela.destroy(),
    width=10,
    bg="#1a1b26",
    fg="#FFFFFF",
    relief="flat",
    justify="center")
# banco de dadoskkk
conn = sqlite3.connect("senhas.db")
cursor = conn.cursor()

try:
    cursor.execute("""
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    senha INTEGER,
    """)
except sqlite3.Error as erro:
    print("Erro: ", erro)
finally:
    conn.close()

# desenhando e atualizando
login.pack(pady=5)
senha.pack(pady=5)
sair.pack(pady=5)

janela.mainloop()
