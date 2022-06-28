for _ in range(int(input())):
  S = input().split()
  N, M = map(int, input().split())
  R = N + M
  if S[1] == "PAR":
    print(f"{S[0] if R % 2 == 0 else S[2]}")
  else:
    print(f"{S[2] if R % 2 == 0 else S[0]}")