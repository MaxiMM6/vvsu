import math

a = float(input())
b = float(input())
c = float(input())

d = pow(b, 2) - (4 * a * c)

if d > 0:
    x1 = float(((b * (-1)) - math.sqrt(d)) / 2 * a)
    x2 = float(((b * (-1)) + math.sqrt(d)) / 2 * a)

    print(x1, x2, sep="\n")

elif d == 0:
    x1 = float(b * (-1) / 2 * a)
    print(x1)

elif d < 0:
    print('Нет корней')

