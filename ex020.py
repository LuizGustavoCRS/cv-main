#from random import sample
from random import shuffle

lista = list()

for elem in range(1,5):
    lista.append(input(f'Digite o nome do {elem}° aluno: '))

#rand = list(sample(lista, k=4))
shuffle(lista)

# for elem in rand:
#     print(f'{rand.index(elem)+1}° aluno escolhido aleatoriamente: {elem}')
for elem in lista:
    print(f'{lista.index(elem)+1}° aluno escolhido aleatoriamente: {elem}')
