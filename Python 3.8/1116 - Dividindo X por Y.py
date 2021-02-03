N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    if X == 0:
        print('0.0')
    elif Y == 0:
        print('divisao impossivel')
    else:
        print(X / Y)
