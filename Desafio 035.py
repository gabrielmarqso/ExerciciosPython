r1 = int(input('Digite o comprimento da 1° reta: '))
r2 = int(input('Digite o comprimento da 2° reta: '))
r3 = int(input('Digite o comprimento da 3° reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triangulo')
