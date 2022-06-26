N = float(input())
N += 0.001

if 0 < N < 1000000.00:
    x1 = N // 100

    y1 = N % 100
    x2 = y1 // 50

    y2 = y1 % 50
    x3 = y2 // 20

    y3 = y2 % 20
    x4 = y3 // 10

    y4 = y3 % 10
    x5 = y4 // 5

    y5 = y4 % 5
    x6 = y5 // 2

    y6 = y5 % 2
    x7 = y6 // 1

    y7 = y6 % 1
    x8 = y7 // 0.50

    y8 = y7 % 0.50
    x9 = y8 // 0.25

    y9 = y8 % 0.25
    x10 = y9 // 0.10

    y10 = y9 % 0.10
    x11 = y10 // 0.05

    y11 = y10 % 0.05
    x12 = y11 // 0.01

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(x1))
print('{:.0f} nota(s) de R$ 50.00'.format(x2))
print('{:.0f} nota(s) de R$ 20.00'.format(x3))
print('{:.0f} nota(s) de R$ 10.00'.format(x4))
print('{:.0f} nota(s) de R$ 5.00'.format(x5))
print('{:.0f} nota(s) de R$ 2.00'.format(x6))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(x7))
print('{:.0f} moeda(s) de R$ 0.50'.format(x8))
print('{:.0f} moeda(s) de R$ 0.25'.format(x9))
print('{:.0f} moeda(s) de R$ 0.10'.format(x10))
print('{:.0f} moeda(s) de R$ 0.05'.format(x11))
print('{:.0f} moeda(s) de R$ 0.01'.format(x12))
