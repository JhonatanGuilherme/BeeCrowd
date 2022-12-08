"""Division of Nlogonia"""
while True:
  K = int(input())
  if K == 0: break

  N, M = map(int, input().split())
  for _ in range(K):
    X, Y = map(int, input().split())
    if X in [N, M] or Y in [N, M]:
      print("divisa")
      continue
    output = "N" if Y > M else "S"
    output += "E" if X > N else "O"
    print(output)
