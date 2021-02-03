lista = []
for i in range(10):
    X = int(input())
    lista.append(X)
    if lista[i] <= 0:
        lista[i] = 1
for i in range(10):
    print('X[{}] = {}'.format(i, lista[i]))
