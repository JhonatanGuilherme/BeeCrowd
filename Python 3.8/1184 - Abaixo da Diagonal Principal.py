M = []
O = input()
X = 0
for i in range(12):
    for j in range(12):
        M = float(input())
        if i > j:
            X += M
if O == 'S':
    print('{:.1f}'.format(X))
elif O == 'M':
    print('{:.1f}'.format(X/66))
