A, B = map(int, input().split())
if B > A:
    print('O JOGO DUROU {} HORA(S)'.format(B - A))
else:
    C = (24 - A) + B
    print('O JOGO DUROU {} HORA(S)'.format(C))
