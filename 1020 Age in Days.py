D=int(input())
a=D//365
m=(D%365)//30
d=((D%365)%30)
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(a,m,d))
