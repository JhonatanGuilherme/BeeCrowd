T = int(input())
for i in range(T):
    PA, PB, G1, G2 = map(float, input().split())
    X, Y, CONTADOR = PA, PB, 0
    while True:
        X += int(PA * (G1 / 100))
        Y += int(PB * (G2 / 100))
        PA = X
        PB = Y
        CONTADOR += 1
        if CONTADOR > 100 or PA > PB:
            break
    if CONTADOR > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(CONTADOR))
