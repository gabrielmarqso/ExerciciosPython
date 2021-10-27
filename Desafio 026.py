frase = str(input('Digite a frase: '))
print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('Ela aparece primeiro na posição {}'.format(frase.upper().find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))