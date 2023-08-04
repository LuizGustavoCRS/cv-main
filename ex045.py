from random import choice
loop = 0
lista = ['papel', 'pedra', 'tesoura']

while loop == 0:
    bot = choice(lista)
    jogador = (input('Escolha papel, pedra ou tesoura: '))

    if jogador in lista:
        if jogador == 'pedra' and bot == 'tesoura' or jogador == 'papel' and bot == 'pedra' or jogador == 'tesoura' and bot == 'papel':
            print(f'Escolhi {bot}, Você ganhou!!!')
            loop = 1
        elif jogador == bot:
            print(f'Também escolhi {bot}, empatou, vamos tentar novamente.\n')
        else:
            print(f'Escolhi {bot}, eu ganhei, HAHAHAHA!!!!')
            loop = 1
    else:
        print('Valor não aceito\n')
