N = int(input())
for i in range(N):
    CONTADOR = 0
    CONTADOR2 = 0
    X = int(input())
    while True:
        CONTADOR += 1
        if CONTADOR == X:
            break
        if X % CONTADOR == 0:
            CONTADOR2 += CONTADOR
    if CONTADOR2 == X:
        print('{} eh perfeito'.format(X))
    else:
        print('{} nao eh perfeito'.format(X))

