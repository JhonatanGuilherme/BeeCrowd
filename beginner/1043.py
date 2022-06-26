A, B, C = map(float, input().split())
p = A + B + C
a = ((A + B) * C) / 2
if A + B > C and A + C > B and B + C > A:
    print('Perimetro = {:.1f}'.format(p))
else:
    print('Area = {:.1f}'.format(a))
