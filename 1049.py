a=[]
for i in range(0,3):
    a.append(input())
if a[0] == 'vertebrado':
    if a[1] == 'ave':
        if a[2] == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if a[2] == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if a[1] == 'inseto':
        if a[2] == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if a[2] == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')

