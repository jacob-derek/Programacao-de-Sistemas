import os
from time import sleep

def Escrever(arquivo, texto):
    ARQUIVO = open(f"{arquivo}", mode="w", encoding="utf-8")
    ARQUIVO.write(texto)
    ARQUIVO.close()
    sleep(1)


def Ler(arquivo):
    ARQUIVO = open(f"{arquivo}", mode="r", encoding="utf-8")
    conteudo = ARQUIVO.read()
    ARQUIVO.close()    
    print(conteudo)    
    sleep(1)


def AdicionarConteudo(arquivo, texto):
    ARQUIVO = open(f"{arquivo}", mode="a", encoding="utf-8")
    ARQUIVO.write(texto)
    ARQUIVO.close()
    sleep(1)


#main loop
user_file = input("Qual arquivo deseja analisar?: ")

while True:
    os.system("clear")
    user_input = int(input("""Qual operacao realizar?
    1 - Ler
    2 - Escrever
    3 - Escrever ao fim
    4 - Sair
    \n"""))
    
    if user_input == 4:
        break
    elif user_input == 1:
        Ler(user_file)
    elif user_input == 2:
        user_text = input("$ ")
        Escrever(user_file, user_text)
    elif user_input == 3:
        user_text = input("$ ")
        AdicionarConteudo(user_file, user_text)