import json

try:
    with open("alunos.json", mode="r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
except (OSError, json.JSONDecodeError) as erro:
    print(f"Erro ao ler arquivo: {erro}")
    raise SystemExit(1)

alunos = dados["alunos"]
print("Turma: ", dados["turma"])

ids_encontrados = []
aprovados = 0

soma_medias = 0
medias_validas = 0

for aluno in alunos:
    try:
        id_aluno = aluno["id"]
        nome = aluno.get("nome") or "Nome Desconhecido"
        notas = aluno["notas"]

        if aluno["id"] in ids_encontrados:
            print("ID duplicado: ", aluno["id"])
        ids_encontrados.append(aluno["id"])

        if not isinstance(notas, list) or not notas:
            raise ValueError("Notas ausentes ou lista vazia")
    
        if any(not isinstance(n, (int, float)) or isinstance(n, bool) for n in notas):
            raise TypeError("Notas contem valores nao numericos")

        media = sum(notas) / len(notas)
        if not isinstance("ativo", bool):
            raise TypeError("O campo 'ativo' precisa ser booleano")

        situacao = "Ativo" if ativo else "Inativo"
        resultado = "Aprovado" if media >= 7 else "Reprovado"

        if media >= 7:
            aprovados += 1

        soma_medias += media
        medias_validas += 1

        print(f"{nome}: {media:.1f} | {situacao} | {resultado}")

    except(KeyError, TypeError, ValueError, ZeroDivisionError) as erro:
        print(f"Registro invalido: {erro}")

print("Total de alunos:", len(aluno))
print("Medias calculadas: ", medias_validas)

if medias_validas:
    print("Média geral:", soma_medias / medias_validas)
else:
    print("Media geral: indisponivel")

print("Aprovados:", aprovados)
