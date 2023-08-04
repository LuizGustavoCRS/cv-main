casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o salário do comprador: '))
anos = int(input('Quantos anos ele vai pagar: '))

valor_mensal = casa / (anos * 12)
porcentagem = sal * 0.3


print(f'\nvalor mensal: {valor_mensal:.2f}'
      f'\n30% do salário: {porcentagem}')


print('\nImprestivo aceito' if valor_mensal < porcentagem
      else 'Imprestimo negado')








