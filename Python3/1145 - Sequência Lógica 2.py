X, Y = map(int, input().split())
CONTADOR = 1
for i in range(1, Y + 1):
    if X == CONTADOR:
        print(i)
        CONTADOR = 1
    else:
        print(i, end=' ')
        CONTADOR += 1
