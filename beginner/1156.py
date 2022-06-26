S = 1
CONTADOR = 1
CONTADOR2 = 1
while True:
    CONTADOR += 2
    CONTADOR2 *= 2
    S += CONTADOR / CONTADOR2
    if CONTADOR == 39:
        break
print('{:.2f}'.format(S))
