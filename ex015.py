km = float(input('quantidade de Km percorridos: '))
d = int(input('quantidade de dias: '))

preco_total = (60 * d) + (0.15 * km)

print(f'preço a pagar R$ {preco_total:.2f}')
