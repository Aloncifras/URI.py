a, b, c = [float(i) for i in input().split()]

if a+b>c and a+c>b and b+c>a:
    print(f'Perimetro = {a+b+c}')
else:
    print(f'Area = {(a+b)*c/2}')