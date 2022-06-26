N = int(input())
CONTADOR = 0
while True:
    CONTADOR += 1
    if CONTADOR > N:
        break
    elif N % CONTADOR == 0:
        print(CONTADOR)
