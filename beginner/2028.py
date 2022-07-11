counter = 1
while True:
  try:
    N = input()
  except EOFError: break
  N = int(N)
  S = ''
  for i in range(N + 1):
    S += (str(i) + ' ') * (1 if i == 0 else i)
  numbers = len(S[:-1].split(" "))
  print(f"Caso {counter}: {numbers} numero{'' if numbers == 1 else 's'}")
  print(S[:-1] + '\n')
  counter += 1
