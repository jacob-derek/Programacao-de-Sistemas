#receber arquivo e contar quantas vogais tem nele

def AnaliseVogais(arquivo):
    vogais = "aeiouAEIOUáéíóúãõâêîôûÁÉÍÓÚÃÕÂÊÎÔÛ"
    vogais_existentes = 0
    
    try:
        with open(f"{arquivo}", mode="r", encoding="utf-8") as ARQUIVO:
            for linha in ARQUIVO:
                for letra in linha:
                    if letra in vogais:
                        vogais_existentes += 1
        print(f"Total de vogais: {vogais_existentes}")
    except FileNotFoundError:
        print("Arquivo nao encontrado")

AnaliseVogais('user_file.txt')

with open('user_file.txt', 'a', encoding='utf-8') as f:
    f.write("DAMN")
