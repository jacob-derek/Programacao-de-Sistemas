perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0

for pergunta in range(len(perguntas)):
    resposta = input(f"{perguntas[pergunta]}S/N: ").upper().strip()
    if resposta == "S":
        respostas_positivas += 1

if respostas_positivas == 5:
    print("assassino")
elif 5 > respostas_positivas > 2:
    print("cumplice")
elif respostas_positivas == 2:
    print("suspeita")
else:
    print("inocente")
