while True:
  try:
    N = input()
  except EOFError:
    break
  print(f"vai ter {'copa' if int(N) == 0 else 'duas'}!")