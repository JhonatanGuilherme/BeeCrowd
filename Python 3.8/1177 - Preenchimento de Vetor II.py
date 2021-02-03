T = int(input())
CONTADOR = 0
for i in range(1000):
    print('N[{}] = {}'.format(i, CONTADOR))
    CONTADOR += 1
    if CONTADOR == T:
        CONTADOR = 0
