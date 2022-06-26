N = int(input())
Z = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X == Y:
        print(0)
    elif X < Y:
        while X < Y:
            X += 1
            if X == Y:
                break
            elif X % 2 != 0:
                Z += X
        print(Z)
        Z = 0
    elif X > Y:
        while X > Y:
            X -= 1
            if X == Y:
                break
            elif X % 2 != 0:
                Z += X
        print(Z)
        Z = 0
