lista = []
for i in range(100):
    lista.append(input())
for i in range(len(lista)):
    if float(lista[i]) <= 10:
        print('A[{}] = {:.1f}'.format(i, float(lista[i])))
