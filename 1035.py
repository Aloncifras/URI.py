A = (str(input()).split())
a = int(A[0])
b = int(A[1])
c = int(A[2])
d = int(A[3])
if b>c and d>a and c+d>a+b and c>0 and d>0 and a%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')