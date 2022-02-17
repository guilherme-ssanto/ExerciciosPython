'''
num = int(input("Digite um número entre 0 e 5 tente acertar o numéro que o computador está pensando: "))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
print("O número que o computador pensou foi {}!".format(escolhido))
if num == escolhido:
    print("O Usuário venceu.")
else:
    print("O usuário perdeu.")
'''

from random import randint
from time import sleep
computador = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(3)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}".format(computador, jogador))
