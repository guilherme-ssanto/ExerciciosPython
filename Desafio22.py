nome = str(input("Digite o seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maíuscula é {}".format(nome.upper()))
print("Seu nome em minúscula é {}".format(nome.lower()))
print("Seu nome completo tem {} caracters".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} caracters".format(len(nome.split()[0])))

