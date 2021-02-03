N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    CONTADOR = 0
    CONTADOR2 = 0
    while CONTADOR2 != Y:
        if X % 2 != 0:
            CONTADOR += X
            CONTADOR2 += 1
            X += 1
        else:
            X += 1
    print(CONTADOR)
