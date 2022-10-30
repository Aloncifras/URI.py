n = int(input())
while n > 0: #loop pra rodar enquanto o numero de testes nao for 0
    c=1 #variavel para numerara as cidades
    d=n #variavel para o numero de casos em cada cidade
    while d>0:
        print('Cidade# {}:'.format(c))
        valores = str(input()).split()
        k=n
        while k>1:
            valor2 = input().split()
            valores = valores + valor2
            k-=1
        pessoas = valores[0:2*n:2]
        agua = valores[1:2*n+1:2]
        print(pessoas)
        print(agua)
        # criar uma variavel p1 = pessoa[0], p2 = pessoa[2] .... p'n' = pessoa[n-1]
        # matematicamente seria algo como p(1,n) = pessoa[0:n]
        # e criar uma variavel a1 = agua[0], a2 = agua[1] ... a'n' = agua[n-1]
        # matematicamente algo como a(1,n) = valores[0:n]
        # essa foi a ideia nao sei se tem como generalizar variaveis, mas se tiver algum modo mais facil pra facilitar os calculos com essas n variaves tmj!
        d-=1
        c+=1
    n-=1

