I=input().split()
a=int(I[0])
b=int(I[1])
c=int(I[2])
''' NAO FUNCIONOU PQ O CARA NAO DEVE GOSTAR DE IF MAS OK
if a>=b and a>=c:
     print('{:.0f} eh o maior'.format(a))
if b>=a and b>=c:
    print('{:.0f} eh o maior'.format(b))
if c>=a and c>=b:
    print('{:.0f} eh o maior'.format(c))
'''
def M(a,b):
    return int((a+b+abs(a-b))/2)
m1=M(a,b)
m2=M(m1,c)
print(m2,'eh o maior')