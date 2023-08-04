num = int(input('Digite um número inteiro: '))

escolha = int(input('Deseja converter esse número para qual base?'
                '\n1 - binário'
                '\n2 - octal'
                '\n3 - hexadecimal'
                '\nDigite aqui: '))

if escolha == 1:
    print(bin(num)[2:])
elif escolha == 2:
    print(oct(num)[2:])
elif escolha == 3:
    print(hex(num)[2:])
else:
    print('Digito inválido')