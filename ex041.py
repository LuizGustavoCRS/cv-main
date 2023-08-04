from datetime import datetime

ano = int(input('Digite seu ano de nascimento: '))
ano = datetime.now().year - ano

if ano <= 9:
    print('Mirim')
elif ano <= 14:
    print('Infantil')
elif ano <= 19:
    print('Junior')
elif ano <= 20:
    print('Sênior')
else:
    print('Master')
