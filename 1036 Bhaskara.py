n=0
while n==0:
    A=input('Coloque sua equação na forma Ax^2+Bx+C=0, e coloque em ordem \"A B C\"').split()
    a=float(A[0])
    b=float(A[1])
    c=float(A[2])
    D=(b**2)-(4*a*c)
    if a==0:
        print('Equação de primeiro grau, raiz =',(-c)/b)
    elif D<0:
        print('Impossivel calcular, descriminante menor que 0')
    else:
        x1=((-b)+(D**(1/2)))/(2*a)
        x2=((-b)-(D**(1/2)))/(2*a)
        print('Raiz 1 = {}\nRaiz 2 = {}'.format(x1,x2))
