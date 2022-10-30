from math import gcd
n=int(input())
while n>0:
    L=input().split()
    N1=int(L[0])
    D1=int(L[2])
    O=L[3]
    N2=int(L[4])
    D2=int(L[6])
    SP = N1 * D2 + N2 * D1
    sP = N1 * D2 - N2 * D1
    PD = D1 * D2
    PN = N1 * N2
    if O == '+':
        print('{}/{} = {:.0f}/{:.0f}'.format(SP,PD,SP/gcd(SP,PD),PD/gcd(SP,PD)))
    if O == '-':
        print('{}/{} = {:.0f}/{:.0f}'.format(sP,PD,sP/gcd(sP,PD),PD/gcd(sP,PD)))
    if O == '*':
        print('{}/{} = {:.0f}/{:.0f}'.format(PN,PD,PN/gcd(PN,PD),PD/gcd(PN,PD)))
    if O == '/':
        print('{}/{} = {:.0f}/{:.0f}'.format((N1*D2),(N2*D1),(N1*D2)/gcd((N1*D2),(N2*D1)),(N2*D1)/gcd((N1*D2),(N2*D1))))
    n-=1