nome = input('Digite seu nome completo: ').strip()

print(f'\nnome com letras maiúsculas: {nome.upper()}'
      f'\nnome com letras minúsculas: {nome.lower()}'
      f'\nquantidade de letras sem espaço: {len(nome.replace(" ",""))}'
      f'\nquantidade de letras do primeiro nome: {len(nome.split()[0])}')
