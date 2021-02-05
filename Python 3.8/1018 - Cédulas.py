N = int(input())
if 0 < N < 1000000:
  print(N)
  x1 = N // 100
  print('{} nota(s) de R$ 100,00'.format(x1))
  y1 = N % 100
  x2 = y1 // 50
  print('{} nota(s) de R$ 50,00'.format(x2))
  y2 = y1 % 50
  x3 = y2 // 20
  print('{} nota(s) de R$ 20,00'.format(x3))
  y3 = y2 % 20
  x4 = y3 // 10
  print('{} nota(s) de R$ 10,00'.format(x4))
  y4 = y3 % 10
  x5 = y4 // 5
  print('{} nota(s) de R$ 5,00'.format(x5))
  y5 = y4 % 5
  x6 = y5 // 2
  print('{} nota(s) de R$ 2,00'.format(x6))
  y6 = y5 % 2
  x7 = y6 // 1
  print('{} nota(s) de R$ 1,00'.format(x7))
