#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: '))
print('O novo preço do produto com 5% de desconto é: R${:.2f}'.format(p-(p*(5/100))))