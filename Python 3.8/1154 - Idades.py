IDADE = 0
CONTADOR = 0
CONTADOR2 = 0
while True:
    IDADE = int(input())
    if IDADE < 0:
        break
    CONTADOR += IDADE
    CONTADOR2 += 1
print('{:.2f}'.format(CONTADOR / CONTADOR2))
