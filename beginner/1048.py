x = float(input())
if 0 <= x <= 400:
  reajuste = 0.15
elif 400 < x <= 800:
  reajuste = 0.12
elif 800 < x <= 1200:
  reajuste = 0.10
elif 1200 < x <= 2000:
  reajuste = 0.07
elif x > 2000:
  reajuste = 0.04

nreajuste = x * reajuste
salario = nreajuste + x
print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(nreajuste))
print('Em percentual: {:.0f} %'.format(reajuste * 100))
