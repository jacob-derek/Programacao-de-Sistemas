#input de vogal e verificar qnts vezes
# a vogal aparece num arquivo

def AnaliseLetra(arquivo):
    user_char = input("Digite uma vogal: ")
    total_chars = 0

    try:
        with open(f'{arquivo}', mode='r', encoding='utf-8') as ARQUIVO:
            for linha in ARQUIVO:
                for letra in linha:
                    if letra == user_char:
                        total_chars += 1
        print(total_chars)
    except:
        print("damn")

AnaliseLetra('teste.txt')