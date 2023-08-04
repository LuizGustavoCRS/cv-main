lista = []

for n in range(3):
    lista.append(int(input(f'Digite {n+1}° comprimento: ')))

lista.sort()

print('possível formar um triângulo' if lista[0] + lista[1] > lista[-1]
      else 'impossível formar um triângulo')
