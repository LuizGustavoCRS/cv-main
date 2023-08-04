from random import choice

lista = list()

for elem in range(1,5):
    lista.append(input(f'Digite o nome do {elem}° aluno: '))

print(f'\naluno escolhido aleatoriamente: {choice(lista)}')
