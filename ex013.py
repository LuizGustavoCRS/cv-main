sal_atual = float(input('salário atual: '))
aumento = float(input('porcentagem de aumento: '))

novo_salario = sal_atual * (aumento / 100 + 1)

print(f'\nnovo salário: R${novo_salario:.2f}')
