while True:
    digitos=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a,b=[str(i) for i in input().split()]
    if a==b=='0':
        break
    x=int(a)
    y=int(b)
    while x<=y:
        for i in range(0,10):
            j=str(i)
            h=a.count(j)
            if h!=0:
                s=digitos[i]+h
                digitos.pop(i)
                digitos.insert(i,s)
        x+=1
        a=str(x)
    for i in digitos:
        print(i,end=' ')
    print()

