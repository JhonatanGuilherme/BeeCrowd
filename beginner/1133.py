X = int(input())
Y = int(input())
Z = 0
if X > Y:
    Z = Y
    Y = X
    X = Z
while True:
    X += 1
    if X == Y:
        break
    if X % 5 == 2 or X % 5 == 3:
        print(X)
