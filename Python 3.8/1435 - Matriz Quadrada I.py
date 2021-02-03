while True:
    N = int(input())
    if (N == 0):
        break
    resultado =  []
    for a in range(N):
        matriz = []
        for j in range(N):
            matriz.append(1)
        resultado.append(matriz)
    valor, cima, esquerda, baixo, direita = 1, 0, 0, N - 1, N - 1
    if N % 2 == 0:
        meio = N / 2
    else:
        meio = (N + 1) / 2
    while valor <= meio:
        a = esquerda
        while a <= direita:
            resultado[cima][a] = valor
            resultado[baixo][a] = valor
            a += 1
        a = cima + 1
        while a < baixo:
            resultado[a][esquerda] = valor
            resultado[a][direita] = valor
            a += 1
        valor += 1
        cima += 1
        baixo -= 1
        esquerda += 1
        direita -= 1
    for a in range(N):
        tx = ''
        for j in range(N):
            tx += "%4.d"%resultado[a][j]
        print(tx[1:])
    print("")
