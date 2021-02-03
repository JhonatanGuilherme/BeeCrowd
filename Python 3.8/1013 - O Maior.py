a, b, c = map(int, input().split())
MaiorAB = (a + b + abs(a - b)) / 2
Resultado = (MaiorAB + c + abs(MaiorAB - c)) / 2
print('{:.0f} eh o maior'.format(Resultado))
