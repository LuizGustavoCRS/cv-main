num = int(input('Distância da viagem em kilometros: '))

if num <= 200:
    print(f'Preço da viagem foi R${num * 0.5}')
else:
    print(f'Preço da viagem foi R${num * 0.45}')
