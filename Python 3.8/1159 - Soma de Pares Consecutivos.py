X = 1
CONTADOR = 0
CONTADOR2 = 0
while True:
    X = int(input())
    CONTADOR = 0
    CONTADOR2 = 0
    if X == 0:
        break
    while CONTADOR2 != 5:
        if X % 2 == 0:
            CONTADOR += X
            CONTADOR2 += 1
            X += 1
        else:
            X += 1
    print(CONTADOR)
