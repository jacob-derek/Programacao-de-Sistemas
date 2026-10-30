from random import randint
notas = []

for i in range(4):
    notas.append(randint(0, 10))

print(notas)
print(f"Media: {sum(notas)/len(notas)}")