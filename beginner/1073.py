N = int(input())
X = 2
if 5 < N < 2000:
    while X <= N:
        print('{}^2 = {}'.format(X, X**2))
        X += 2
