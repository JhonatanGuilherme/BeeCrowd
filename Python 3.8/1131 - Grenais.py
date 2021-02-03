INTER = 0
GREMIO = 0
EMPATE = 0
CONTADOR = 0
PARTIDAS = 0
while CONTADOR == 0:
    X, Y = map(int, input().split())
    PARTIDAS += 1
    Z = 0
    if X > Y:
        INTER += 1
    elif X < Y:
        GREMIO += 1
    elif X == Y:
        EMPATE += 1
    print('Novo grenal (1-sim 2-nao)')
    while True:
        Z = int(input())
        if Z == 1:
            CONTADOR = 0
            break
        elif Z == 2:
            CONTADOR += 1
            break
        else:
            Z = int(input())
print('{} grenais'.format(PARTIDAS))
print('Inter:{}'.format(INTER))
print('Gremio:{}'.format(GREMIO))
print('Empates:{}'.format(EMPATE))
if X > Y:
    print('Inter venceu mais')
elif X < Y:
    print('Gremio venceu mais')
elif X == Y:
    print('Nao houve vencedor')
