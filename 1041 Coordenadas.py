x,y=[float(i) for i in (input().split())]
print('Q1') if x>0 and y>0 else 0
print('Q2') if x<0 and y>0 else 0
print('Q3') if x<0 and y<0 else 0
print('Q4') if x>0 and y<0 else 0
print('Origem') if x==y==0 else 0
print('Eixo X') if y==0 and x!=0 else 0
print('Eixo Y') if x==0 and y!=0 else 0



