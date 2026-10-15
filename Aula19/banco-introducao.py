#open() 'W", WR"

arquivo = open("exemplo.json", mode="a", encoding="utf-8")
arquivo.write("Olá mundo!")

for i in range(5):
    arquivo.write(f"\nfds numero {i}")

arquivo.close()
