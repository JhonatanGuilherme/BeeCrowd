N1, N2, N3, N4 = map(float, input().split())
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')
elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {}'.format(exame))
    media2 = (exame + media) / 2
    if media2 >= 5.0:
        print('Aluno aprovado.')
    elif media2 <= 4.9:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media2))

else:
    print('Aluno reprovado.')
