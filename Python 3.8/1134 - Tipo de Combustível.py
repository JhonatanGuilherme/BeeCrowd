ALCOOL = 0
GASOLINA = 0
DIESEL = 0
X = 0
while True:
    X = int(input())
    if X == 1:
        ALCOOL += 1
    elif X == 2:
        GASOLINA += 1
    elif X == 3:
        DIESEL += 1
    elif X == 4:
        print('MUITO OBRIGADO')
        print('Alcool: {}'.format(ALCOOL))
        print('Gasolina: {}'.format(GASOLINA))
        print('Diesel: {}'.format(DIESEL))
        break
