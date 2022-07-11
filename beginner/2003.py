while True:
  try:
    H = list(map(int, input().split(":")))
  except EOFError: break

  M = H[0] * 60 + H[1]
  X = M - (7 * 60)
  print(f"Atraso maximo: {0 if X < 0 else X}")