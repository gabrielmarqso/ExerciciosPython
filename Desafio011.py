#Faça um programa que leia a largura e a altura de
#uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de
#tinta, pinta uma área de 2m²
l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
print ('A área é de {:.2f}m², será necessário {:.2f} litro(s) para pintar essa área.'.format(l*a, l*a/2))