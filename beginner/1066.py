n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
a = 0
b = 0
c = 0
d = 0
if n1 % 2 == 0:
    a += 1
else:
    b += 1
if n1 > 0:
    c += 1
elif n1 < 0:
    d += 1

if n2 % 2 == 0:
    a += 1
else:
    b += 1
if n2 > 0:
    c += 1
elif n2 < 0:
    d += 1

if n3 % 2 == 0:
    a += 1
else:
    b += 1
if n3 > 0:
    c += 1
elif n3 < 0:
    d += 1

if n4 % 2 == 0:
    a += 1
else:
    b += 1
if n4 > 0:
    c += 1
elif n4 < 0:
    d += 1

if n5 % 2 == 0:
    a += 1
else:
    b += 1
if n5 > 0:
    c += 1
elif n5 < 0:
    d += 1

print('{} valor(es) par(es)'.format(a))
print('{} valor(es) impar(es)'.format(b))
print('{} valor(es) positivo(s)'.format(c))
print('{} valor(es) negativo(s)'.format(d))
