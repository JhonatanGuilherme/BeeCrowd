IMPAR = []
PAR = []
for i in range(15):
    X = int(input())
    if X % 2 == 0:
        PAR.append(X)
    elif X % 2 != 0:
        IMPAR.append(X)
    if len(PAR) == 5:
        Y = 0
        for j in PAR:
            print('par[{}] = {}'.format(Y,j))
            Y += 1
        PAR = []
    if len(IMPAR) == 5:
        Y = 0
        for j in IMPAR:
            print('impar[{}] = {}'.format(Y,j))
            Y += 1
        IMPAR = []
if len(IMPAR) > 0:
    Y = 0
    for j in IMPAR:
        print('impar[{}] = {}'.format(Y,j))
        Y += 1
if len(PAR) > 0:
    Y = 0
    for j in PAR:
        print('par[{}] = {}'.format(Y,j))
        Y += 1
