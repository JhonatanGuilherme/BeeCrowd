while True:
  try:
    L = input()
  except EOFError:
    break
  L = int(L)
  V = max(list(map(int, input().split())))
  if V < 10:
    print(1)
  elif V < 20:
    print(2)
  else:
    print(3)