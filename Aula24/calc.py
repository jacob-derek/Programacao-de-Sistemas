# tenho que criar uma calculadora usando tkinter
import tkinter as tk

# ── Paleta de Cores (Estilo Tokyo Night / JBar) ──
BG_DARK = "#16161e"     # Fundo principal da janela
BG_ELEMENT = "#1a1b26"  # Fundo dos inputs e botões
FG_TEXT = "#a9b1d6"     # Cor do texto principal
DIM_TEXT = "#565f89"    # Cor para textos secundários
ACCENT = "#7aa2f7"      # Azul de destaque
GREEN = "#9ece6a"       # Verde para sucesso/resultado
RED = "#f7768e"         # Vermelho para erros

# funcao com as operacoes
def Calcular(operacao):
    try:
        a = float(numero_a.get())
        b = float(numero_b.get())
        
        if operacao == "+":
            resultado = a + b
        elif operacao == "-":
            resultado = a - b
        elif operacao == "*":
            resultado = a * b
        elif operacao == "/":
            resultado = a / b  if b != 0 else "Erro (div por 0)"
        
        label_resultado.config(text=f"Resultado: {resultado}", fg=GREEN) # atualizando resultado
        
    except ValueError:
        label_resultado.config(text="Digite numeros validos.", fg=RED) # atualizando resultado por erro


window = tk.Tk()
window.title("JCalc")
window.geometry("320x380")
window.configure(bg=BG_DARK)

titulo = tk.Label(window, text="CALCULADORA", bg=BG_DARK, fg=DIM_TEXT, font=("Segoe UI", 10,"bold"))
titulo.pack(pady=(20, 10))

numero_a = tk.Entry(window, width=18, font=("Segoe UI", 14), bg=BG_ELEMENT, fg=FG_TEXT, insertbackground=FG_TEXT, relief="flat", justify="center")
numero_b = tk.Entry(window, width=18, font=("Segoe UI", 14), bg=BG_ELEMENT, fg=FG_TEXT, insertbackground=FG_TEXT, relief="flat", justify="center")
window.resizable(False, False)

numero_a.pack(pady=5, ipady=5)
numero_b.pack(pady=5, ipady=5)

frame_botoes = tk.Frame(window, bg=BG_DARK)
frame_botoes.pack(pady=10)

btn_config = {
    "width": 5,
    "height": 2,
    "font": ("Segoe UI", 12, "bold"),
    "bg": BG_ELEMENT,
    "fg": ACCENT,
    "activebackground": ACCENT,
    "activeforeground": BG_DARK,
    "relief": "flat",
    "cursor": "hand2"
}

btn_soma = tk.Button(frame_botoes, text="+", command=lambda: Calcular("+"), **btn_config)
btn_sub = tk.Button(frame_botoes, text="-", command=lambda: Calcular("-"), **btn_config)
btn_mult = tk.Button(frame_botoes, text="*", command=lambda: Calcular("*"), **btn_config)
btn_div = tk.Button(frame_botoes, text="/", command=lambda: Calcular("/"), **btn_config)

btn_soma.grid(row = 0, column = 0, padx = 6, pady = 6)
btn_sub.grid(row = 0, column = 1, padx = 6, pady = 6)
btn_mult.grid(row = 1, column = 0, padx = 6, pady = 6)
btn_div.grid(row = 1, column = 1, padx = 6, pady = 6)

label_resultado = tk.Label(window, text="Resultado: ", font=("Segue UI", 14, "bold"), bg=BG_DARK, fg=FG_TEXT)
label_resultado.pack(pady=10)
window.mainloop()