preco = float(input('Digite o preço do produto: '))
metodo_pagamento = int(input('\n1. À vista no dinheiro'
                             '\n2. À vista no cartão'
                             '\n3. 2x no cartão'
                             '\n4. 3x ou mais no cartão'
                             '\nMetodo de pagamento:'))

if metodo_pagamento == 1:
    print(f'\npreço total: R$ {preco * 0.9}')
if metodo_pagamento == 2:
    print(f'\npreço total: R$ {preco * 0.95}')
if metodo_pagamento == 3:
    print(f'\npreço total: R$ {preco}')
if metodo_pagamento == 4:
    print(f'\npreço total: R$ {preco * 1.2}')
else:
    print('\nForma de pagamento incorreto')