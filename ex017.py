# from math import sqrt, pow
from math import hypot

co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))

#hip = sqrt(pow(co, 2) + pow(ca, 2))
hip = hypot(co, ca)

print(f'hipotenusa: {hip}')
