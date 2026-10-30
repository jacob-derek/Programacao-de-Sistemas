from random import randint

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas_por_meses = [randint(15, 35) for _ in range(len(meses))]
temperatura_media_anual = sum(temperaturas_por_meses) / len(temperaturas_por_meses)

for i in range(len(meses)):
    if temperaturas_por_meses[i] > temperatura_media_anual:
        print(f"{i + 1} - {meses[i]}: {temperaturas_por_meses[i]}°C")