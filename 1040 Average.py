a, b, c, d  = [float(i) for i in input().split()]
media = (2*a+3*b+4*c+d)/10
print(f'Media: {media:.1f}')
print('Aluno aprovado.') if media >= 7 else 0
print('Aluno reprovado.') if media < 5 else 0
if 5 <= media < 7:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    print('Aluno aprovado.') if media >= 5 else 0
    print('Aluno reprovado.') if media < 5 else 0
    print(f'Media final: {(media+exame)/2}')
