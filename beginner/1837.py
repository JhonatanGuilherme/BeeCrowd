A, B = map(float, input().split())
if A > 0:
  Q = int(A / B)
  print(Q, int(-(B * Q - A)))
else:
  print(int(A // B), int(A % B))