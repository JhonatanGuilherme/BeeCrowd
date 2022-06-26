from math import sqrt
A, B, C = map(float, input().split())
if A != 0:
    D = (B * B) - (4 * A * C)
    if D > 0:
        X = (-B + sqrt(D)) / (2 * A)
        Y = (-B - sqrt(D)) / (2 * A)
        print('R1 = {:.5f}'.format(X))
        print('R2 = {:.5f}'.format(Y))
    elif D < 0:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')
