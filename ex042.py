lista = []

for n in range(3):
    lista.append(int(input(f'Digite {n+1}° comprimento: ')))

lista.sort()

if lista[0] + lista[1] > lista[-1]:
    if lista[0] == lista[1] == lista[2]:
        print('Equilátero')
    elif lista[0] != lista[1] != lista[2]:
        print('Escaleno')
    else:
        print('Isósceles')
else:
     print('impossível formar um triângulo')
