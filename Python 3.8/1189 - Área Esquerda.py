M = []
O = input()
X = 0
for i in range(12):
    for j in range(12):
        M = float(input())
        if i > j and i + j <= 10:
            X += M
if O == 'S':
    print('{:.1f}'.format(X))
elif O == 'M':
    print('{:.1f}'.format(X/30))
