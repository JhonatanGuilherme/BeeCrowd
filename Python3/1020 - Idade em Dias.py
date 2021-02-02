D = int(input())
A = int(D / 365)
D -= A * 365
M = int(D / 30)
D -= M * 30
print('{} ano(s)'.format(A))
print('{} mes(es)'.format(M))
print('{} dia(s)'.format(D))
