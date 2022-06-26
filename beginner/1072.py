N = int(input())
x = 0
y = 0
for i in range(N):
  X = int(input())
  if 10 <= X <= 20:
    x += 1
  else:
    y += 1
print('{} in'.format(x))
print('{} out'.format(y))
