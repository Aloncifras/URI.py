T = input().split()
a=float(T[0])
b=float(T[1])
c=float(T[2])
pi=3.14159
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(a*c/2,pi*c**2,(a+b)*c/2,b**2,a*b))