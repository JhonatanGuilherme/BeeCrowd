I = 1
J = 7
x = 0
while I < 10:
    print('I={} J={}'.format(I, J))
    J -= 1
    x += 1
    if x == 3:
        I += 2
        J += 5
        x = 0
