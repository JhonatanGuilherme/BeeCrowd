Y = 0
soma = 0
while True:
    X = 0
    while soma < 2:
        Z = float(input())
        if 0 <= Z <= 10:
            soma += 1
            Y += Z
        else:
            print('nota invalida')
    print('media = {:.2f}'.format(Y / 2))
    while X != 1 and X != 2:
        print('novo calculo (1-sim 2-nao)')
        X = int(input())
    if X == 1:
        soma = 0
        Y = 0
    elif X == 2:
        break
