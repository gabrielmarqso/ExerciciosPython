import random
n1 = input('Digite o 1° nome: ')
n2 = input('Digite o 2° nome: ')
n3 = input('Digite o 3° nome: ')
n4 = input('Digite o 4° nome: ')
lista = [n1,n2,n3,n4]
print('O {} foi escolhido no sorteio'.format(random.choice(lista)))