lista = []
CONTADOR = 19
for i in range(20):
    lista.append(int(input()))
for i in range(len(lista)):
    print('N[{}] = {}'.format(i, lista[i + CONTADOR]))
    CONTADOR -= 2
