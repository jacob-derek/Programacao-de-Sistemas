#receber arquivo
#copiar tudo dele
#substituir as vogais por *

vogais = "aeiouAEIOU"
with (open("teste.txt", mode="r", encoding="utf-8") as MAIN_FILE, 
    open("copia_teste.txt", mode="w", encoding="utf-8") as COPIA_FILE):
        for linha in MAIN_FILE:
            linha_modificada = ""
            for letra in linha:
                if letra in vogais:
                    linha_modificada += '*'
                else:
                    linha_modificada += letra
            COPIA_FILE.write(linha_modificada)
            print(linha_modificada)