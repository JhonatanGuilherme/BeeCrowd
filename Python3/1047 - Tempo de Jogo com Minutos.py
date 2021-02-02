A, B, C, D = map(int, input().split())
x = A * 60 + B
y = C * 60 + D
if A <= C:
  z = y - x
  if z == 0:
    print('O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)'.format(24, z % 60))
  else:
    print('O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)'.format((z - z % 60) / 60, z % 60))
else:
  z = (24 * 60 - x) + y
  print('O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)'.format((z - z % 60) / 60, z % 60))
