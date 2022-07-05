P, N = map(int, input().split())
H = list(map(int, input().split()))

frog_can_reach = True
for i in range(N - 1):
  if abs(H[i] - H[i + 1]) > P:
    frog_can_reach = False
print("YOU WIN" if frog_can_reach else "GAME OVER")