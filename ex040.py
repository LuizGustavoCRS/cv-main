n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('\033[;31mReporvado')
elif media < 6.9:
    print('\033[;32mRecuperação')
else:
    print('\033[;34mAprovado')