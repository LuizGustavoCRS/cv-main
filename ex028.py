from random import randrange

num = int(input('Digite um número de 1 a 5: '))
print('acertou!' if num == randrange(5)+1 else 'errou!')
