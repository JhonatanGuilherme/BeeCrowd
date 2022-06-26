while True:
  try:
    N = input()
  except EOFError: break
  
  N = int(N)
  N_divided_by_2 = int(N / 2)
  N_divided_by_3 = int(N / 3)
  for i in range(N):
    for j in range(N):
      if N_divided_by_2 == i and N_divided_by_2 == j:
        print(4, end="")
      elif i >= N_divided_by_3 and j >= N_divided_by_3 and i < N - N_divided_by_3 and j < N - N_divided_by_3:
        print(1, end="")
      elif i == j:
        print(2, end="")
      elif i + j == N - 1:
        print(3, end="")
      else:
        print(0, end="")
    print("")
  print("")