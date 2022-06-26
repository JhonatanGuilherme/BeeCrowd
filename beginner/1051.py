x = float(input())
if 0 < x <= 2000:
    print('Isento')
elif 2000 < x <= 3000:
    y = x - 2000
    r = y * 0.08
    print('R$ {:.2f}'.format(r))
elif 3000 < x <= 4500:
    y = x - 3000
    r = y * 0.18
    print('R$ {:.2f}'.format(r + 80))
else:
    y = x - 4500
    r = y * 0.28
    print('R$ {:.2f}'.format(r + 80 + 270))
