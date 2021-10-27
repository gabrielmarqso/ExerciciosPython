salario = float(input('Qual o seu salário? : '))

if salario > 1.250:
    print('Você receberá um aumento de 10%')
    print('Agora seu salário será de R$ {} .'.format(salario + (salario * 10 / 100)))
else:
    print('Você receberá um aumento de 15%')
    print('Agora seu salário será de R$ {} .'.format(salario + (salario * 15 / 100)))
