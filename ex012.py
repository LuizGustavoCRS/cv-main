preco = float(input('preço do produto: '))
desconto = float(input('desconto em porcentagem: '))

pcd = preco * (100-desconto) / 100

print(f'preço com desconto:  R${pcd:.2f}')
