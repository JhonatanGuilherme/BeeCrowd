N = int(input())
X = list(map(int, input().split()))

position = stars_attacked = sheep_counter = 0
while True:
  sheeps_in_position = X[position]
  if not sheeps_in_position:
    break
  stars_attacked += 1
  sheep_counter += sheep_counter
print(f"{stars_attacked} {sheep_counter}")