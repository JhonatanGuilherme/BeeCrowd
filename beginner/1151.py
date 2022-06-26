FIBONACCI = '0'
N = int(input())
Y = 0
Z = 1
LISTA = [Y, Z]
for i in range(N - 2):
    X = Y + Z
    Y = Z
    Z = X
    LISTA.append(X)
for i in range(N - 1):
    FIBONACCI += ' ' + str(LISTA[i + 1])
print(FIBONACCI)
