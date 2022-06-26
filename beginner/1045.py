A, B, C = map(float, input().split())
lista = A, B, C
A, B, C = sorted(lista)[::-1]
if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A ** 2 == (B ** 2 + C ** 2):
        print('TRIANGULO RETANGULO')
    if A ** 2 > (B ** 2 + C ** 2):
        print('TRIANGULO OBTUSANGULO')
    if A ** 2 < (B ** 2 + C ** 2):
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B != C or B == C != A or C == A != B:
        print('TRIANGULO ISOSCELES')
