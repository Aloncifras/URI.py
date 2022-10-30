#input Codigo / Unidades / preço/un
o1=str(input()).split()
o2=str(input()).split()
u1=int(o1[1])
u2=int(o2[1])
p1=float(o1[2])
p2=float(o2[2])
t=u1*p1+u2*p2
print('VALOR A PAGAR: R$ {:.2f}'.format(t))