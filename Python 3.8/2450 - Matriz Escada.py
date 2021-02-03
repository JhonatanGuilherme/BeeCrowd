L = []
N, M = map(int, input().split())

auxiliar, auxiliar2 = True, True
verificador = 0

for i in range(N):
  L.append(list(map(int, input().split())))
  zeros = 0
  auxiliar = True
  for j in range(M):
    if auxiliar and L[i][j] == 0:
      zeros += 1
    else:
      auxiliar = False
  if i != 0:
    if (zeros > verificador or (zeros == verificador and zeros == M)) and auxiliar2:
      verificador = zeros
    else:
      verificador = 0
      auxiliar2 = False
  else:
    verificador = zeros
  
if verificador:
  print("S")
else:
  print("N")