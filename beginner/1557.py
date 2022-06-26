while True:
  N = int(input())
  if N == 0: break

  matrix = []
  first_value = 1
  for i in range(1, N + 1):
    line = []
    for j in range(i, N + i):
      line.append(first_value if len(line) == 0 else line[-1] * 2)
    matrix.append(line)
    if i == N: break
    first_value = line[1]
  
  length_higher_value = len(str(matrix[-1][-1]))
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      space_between_values = (length_higher_value - len(str(matrix[i][j])))
      print(matrix[i][j], " " * space_between_values, end="")
    print("")
  print("")
