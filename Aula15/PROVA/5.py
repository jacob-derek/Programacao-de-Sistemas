from random import randint

alturas_todo = [randint(150, 190) for _ in range(30)]
idade_todos = [randint(10, 20) for _ in range(30)]

media_altura_todos = sum(alturas_todo) / len(alturas_todo)

alunos_passados = 0
for atual in range(30):
    if idade_todos[atual] > 13 and alturas_todo[atual] < media_altura_todos:
        alunos_passados += 1

print(f"Média de altura da turma: {media_altura_todos:.2f}cm")
print(f"Número de alunos com mais de 13 anos abaixo da média: {alunos_passados}")