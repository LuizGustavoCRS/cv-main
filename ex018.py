from math import cos, tan, sin, radians

ang = int(input('digite o ângulo: '))

rad = radians(ang)

print(f'\nseno: {sin(rad):.2f}'
      f'\ncosseno: {cos(rad):.2f}'
      f'\ntangente: {tan(rad):.2f}')

