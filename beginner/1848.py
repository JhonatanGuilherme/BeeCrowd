blink_counter = numbers_sum = scream_counter = 0
while True:
  if scream_counter == 3: break
  S = input()
  if S == "caw caw":
    scream_counter += 1
    print(numbers_sum)
    numbers_sum = 0
  else:
    number = ""
    for blink in S:
      if blink == "-":
        number += "0"
      elif blink == "*":
        number += "1"
    numbers_sum += int(int(number, 2))
    blink_counter += 1
