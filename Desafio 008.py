#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
m = int(input('Quantos metros? '))
print('Essa quantidade de metros equivale a:\n{} centimetros\n{} milimetros'.format(m*100,m*1000))