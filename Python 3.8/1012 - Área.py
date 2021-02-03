A, B, C = map(float, input().split())
TRIANGULO = (A * C) / 2
CIRCULO = (C ** 2) * 3.14159
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = B ** 2
RETANGULO = A * B
print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}'.format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}'.format(RETANGULO))
