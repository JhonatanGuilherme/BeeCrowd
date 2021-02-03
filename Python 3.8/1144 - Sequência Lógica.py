N = int(input())
X = 1
for i in range(N):
    print('{} {} {}'.format(X, X * X, X * X * X))
    print('{} {} {}'.format(X, X * X + 1, X * X * X+ 1))
    X += 1
