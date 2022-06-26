while True:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    elif M > N:
        O = M
        M = N
        N = O
    O = 0
    soma = ''
    while M <= N:
        soma += str(M) + ' '
        O += M
        M += 1
    soma += 'Sum='
    print('{}{}'.format(soma, O))
