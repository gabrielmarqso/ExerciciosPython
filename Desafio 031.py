distancia = float(input('Qual é a distância da viagem em km? '))
if distancia <=200:
    print('O preço da passagem é de R${}'.format(distancia*0.50))
else:
    print('O preço da passagem é de R$ {}'.format(distancia*0.45))
