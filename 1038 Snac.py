I = input().split()
if I[0] == '1':
    r=4
elif I[0] == '2':
    r=4.5
elif I[0] == '3':
    r=5
elif I[0] == '4':
    r=2
else:
    r=1.5
print('Total: R$ {:.2f}'.format(float(r*int(I[1]))))