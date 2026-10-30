from random import choice, randint, shuffle

vetor_a = [randint(1, 100) for _ in range(10)]
vetor_b = [randint(1, 100) for _ in range(10)]

vetor_c = []

print(vetor_a)
print(vetor_b)

while vetor_a:
    item = choice(vetor_a)
    vetor_c.append(item)
    vetor_a.remove(item)

while vetor_b:
    item = choice(vetor_b)
    vetor_c.append(item)
    vetor_b.remove(item)

shuffle(vetor_c)
print(vetor_c)
