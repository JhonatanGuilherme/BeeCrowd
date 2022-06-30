N = int(input())
for _ in range(N):
  T = int(input())
  sub = 2015 - T
  print(f"{abs(sub - 1)} A.C" if sub <= 0 else f"{sub} D.C")