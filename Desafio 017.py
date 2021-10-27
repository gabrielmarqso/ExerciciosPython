#Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjascente: '))
h = math.pow(co,2) + math.pow(ca,2)
print ('O comprimento da hipotenusa é {:.2f}'.format(math.sqrt(h)))