#Faça um progrma que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
ang = float(input('Digite o angulo: '))
rad = math.radians(ang)
print('O seno desse angulo é {:.2f}\nO cosseno {:.2f}\nA tangente {:.2f}\n'.format(math.sin(rad), math.cos(rad), math.tan(rad)))