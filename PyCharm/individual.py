import math
print("Введите длины трёх сторон треугольника")
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Площадь треугольника равна %.2f" % S)