#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostra quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27
d = float(input('Quanto dinheiro você tem carteira?'))
print('Você pode comprar {:.2f} dólares.'.format(d/3.27))