'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
num = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print("O valor de seno é {:.2f}, cosseno {:.2f}, tangente {:.2f}".format(seno, cosseno, tangente))