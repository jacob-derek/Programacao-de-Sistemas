from random import randint

media_todos_alunos = []

for i in range(1, 11):
    notas = [randint(0, 10) for _ in range(4)]
    media = sum(notas) / 4
    media_todos_alunos.append(media)
    print(f"Aluno {i} | Notas: {notas} | Media: {media:.1f}")


alunos_aprovados = 0

for media in media_todos_alunos:
    if media >= 7.0:
        alunos_aprovados += 1


print("\n--- RESULTADO FINAL ---")
print("Lista de todas as médias:", media_todos_alunos)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")