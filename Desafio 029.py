v = int(input('Digite a velocidade do carro: '))
if v >= 80:
    multa = (v-80)*7
    print('Você foi multado no valor de R${},00'.format(multa))
else:
    print('Você estava dirigindo na velocidade correta.')
