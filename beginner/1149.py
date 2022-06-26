LISTA = list(map(int, input().split()))
X = LISTA[0]
CONTADOR = 0
for i in range(len(LISTA)):
    if LISTA[1 + CONTADOR] <= 0:
        CONTADOR += 1
    else:
        Y = LISTA[1 + CONTADOR]
CONTADOR = X
for i in range(1, Y):
    CONTADOR += X + i
print(CONTADOR)
