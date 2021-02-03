N = int(input())
R = 0
S = 0
C = 0
total = 0

for i in range(N):
    x, y = input().split()
    if y == 'R':
        R += int(x)
    elif y == 'S':
        S += int(x)
    elif y == 'C':
        C += int(x)

total = R + S + C
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(C))
print('Total de ratos: {}'.format(R))
print('Total de sapos: {}'.format(S))
print('Percentual de coelhos: {:.2f} %'.format(float(100 * C / total)))
print('Percentual de ratos: {:.2f} %'.format(float(100 * R / total)))
print('Percentual de sapos: {:.2f} %'.format(float(100 * S / total)))
