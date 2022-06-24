import math

while True:
    array = list(map(int, input().split()))
    if array[0] == 0:
        break
    area = array[0] * array[1]
    percent = (array[2]) / 100
    print(int(math.sqrt(area / percent)))
