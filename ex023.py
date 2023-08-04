num = int(input('Digite um número entre 0 e 9999: '))

if len(str(num)) > 4:
    print('\nnúmero maior que o esperado')

if len(str(num)) > 0:

    print(f'\nunidade: {str(num)[-1]}')
    if len(str(num)) > 1:

        print(f'dezena: {str(num)[-2]}')
        if len(str(num)) > 2:

            print(f'centena: {str(num)[-3]}')
            if len(str(num)) > 3:

                print(f'milhar: {str(num)[-4]}')
