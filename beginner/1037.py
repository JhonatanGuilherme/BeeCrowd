X = float(input())
if 0 <= X < 25.01:
    print('Intervalo [0,25]')
elif 25.01 <= X < 50.01:
    print('Intervalo (25,50]')
elif 50.01 <= X < 75.01:
    print('Intervalo (50,75]')
elif 75.01 <= X < 100.01:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
