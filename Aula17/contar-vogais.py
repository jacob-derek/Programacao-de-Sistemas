def ContarVogais(string):
    vogais = ["a","e","i","o","u"]
    lista_palavra = []
    
    for letra in string:
        lista_palavra.append(letra)
    
    for letra in lista_palavra:
        if letra in vogais:
            lista_palavra.remove(letra)
            
    print(lista_palavra
    )

print("abacaxi")
ContarVogais("abacaxi")