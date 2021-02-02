A = 0
B = 1
LISTA = []
LISTA.append(A)
LISTA.append(B)
T = int(input())
for i in range(T):
    N = int(input())
    while len(LISTA) <= N:
        A, B = B, A + B
        LISTA.append(B)
    print('Fib({}) = {}'.format(N, LISTA[N]))
