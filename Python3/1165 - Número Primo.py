N = int(input())
for i in range(N):
    CONTADOR = 0
    X = int(input())
    for j in range(X):
        if X % (j + 1) == 0:
            CONTADOR += 1
    if CONTADOR == 2:
        print('{} eh primo'.format(X))
    else:
        print('{} nao eh primo'.format(X))
