a1 = input().split()
dia1 = int(a1[1])
b1 = input().split()
hora1 = int(b1[0])
min1 = int(b1[2])
sec1 = int(b1[4])

a2 = input().split()
dia2 = int(a2[1])
b2 = input().split()
hora2 = int(b2[0])
min2 = int(b2[2])
sec2 = int(b2[4])

dia = dia2 - dia1
hora = hora2 - hora1
if hora < 0:
    hora += 24
    dia -= 1
min = min2 - min1
if min < 0:
    min += 60
    hora -= 1
sec = sec2 - sec1
if sec < 0:
    sec += 60
    min -= 1
if dia <= 0:
    dia = 0

print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(hora))
print('{} minuto(s)'.format(min))
print('{} segundo(s)'.format(sec))
