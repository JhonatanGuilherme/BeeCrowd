X = int(input())
Y = int(input())
Z = 0
CONTADOR = 0
if X > Y:
    Z = Y
    Y = X
    X = Z
while True:
    if X % 13 != 0:
        CONTADOR += X
    X += 1
    if X > Y:
        break
print(CONTADOR)
