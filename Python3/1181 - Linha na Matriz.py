L = int(input())
M = []
T = input()
X = 0
for i in range(12):
    for j in range(12):
        M = float(input())
        if i == L:
            X += M
if T == 'S':
    print('{:.1f}'.format(X))
elif T == 'M':
    print('{:.1f}'.format(X/12))
