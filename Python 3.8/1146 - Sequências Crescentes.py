while True:
    X = int(input())
    if X == 0:
        break
    Y = '1'
    CONTADOR = 1
    while CONTADOR < X:
        CONTADOR += 1
        Y += ' ' + str(CONTADOR)
    print(Y)
