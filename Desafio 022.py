#Crie um pograma que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas letras minusculas
#Quantas letras ao todo sem considerar espaços.
#Quantas letras tem o primeiro nome.
nome = input('Digite o seu nome completo: ')
print('Seu nome completo em MAIUSCULO É: {}'.format(nome.upper()))
print('Seu nome completo em minúsculo é: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome)-nome.count(' ')))
dividido = nome.split()
primeiro = (dividido[0])
print('Seu primeiro nome tem {} letras'.format(len(primeiro)))