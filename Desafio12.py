v = float(input("Inserir valor do produto R$:"))
d = v - ((v*5)/100)
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(v, d))