CONTADOR = 0
N = int(input())
POSICAO = 0
X = list(map(int, input().split()))
MINIMO = X[0]
for i in X:
    CONTADOR += 1
    if MINIMO > i:
        MINIMO = i
        POSICAO = CONTADOR
print('Menor valor: {}'.format(MINIMO))
print('Posicao: {}'.format(POSICAO - 1))
