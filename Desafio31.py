distancia = float(input("Qual é a distância da sua viagem? "))
print("Você está preste a começar uma viagem de {:.1f}Km".format(distancia))
if distancia >= 200:
    valor = distancia * 0.45
else:
    valor = distancia *0.5
print("E o preço da sua passagem será de {:.2f}".format(valor))
