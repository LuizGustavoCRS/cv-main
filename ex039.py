from datetime import datetime

ano = int(input('Digite seu ano de nascimento: '))
ano = datetime.now().year - ano

if ano < 18:
    print('Muito novo para se alistar')
elif ano == 18:
    print('Ano de se alistar')
else:
    print('Prazo de alistamento ultrapassado')
