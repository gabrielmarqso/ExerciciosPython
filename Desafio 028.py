from random import randint
r = randint(0,5)
guess = int(input('Advinhe qual o número o computador pensou: '))
print('Você acertou' if guess==r else('Você errou, o número foi {}').format(r))
