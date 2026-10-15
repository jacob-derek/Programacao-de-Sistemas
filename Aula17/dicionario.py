dados = {
"Nome": "Jacob",
"Idade": 18,
"Hobbie": "Guitarra"
}

for i in dados:
    print(dados[i])

if "Nome" in dados:
    del dados["Nome"]

print(dados)
