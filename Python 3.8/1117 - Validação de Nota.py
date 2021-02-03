Y = 0
Z = 0
while Z < 2:
    X = float(input())
    if 0.0 <= X <= 10.0:
        Y += X
        Z += 1
    else:
        print('nota invalida')
print('media = {:.2f}'.format(Y / 2))
