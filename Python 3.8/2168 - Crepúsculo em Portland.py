M1, M2, N = [], [], int(input())

for i in range(N + 1):
  M1.append(list(map(int, input().split())))

for i in range(N):
  for j in range(N):
    S = 0
    if M1[i][j] == 1:
      S += 1
    if M1[i][j+1] == 1:
      S += 1
    if M1[i + 1][j] == 1:
      S += 1
    if M1[i + 1][j + 1] == 1:
      S += 1
    if S >= 2:
      print("S", end="")
    else:
      print("U", end="")
  print()
