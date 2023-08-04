vel = int(input('Digite a velocidade do carro: '))

print(f'Multa de R${(vel - 80) * 7} por ultrapassar o limite de 80Km/h.'
      if vel > 80 else
      'Velocidade dentro do limite permitido.')
