a, b, c = [float(i) for i in input().split()]

if a+b>c and a+c>b and b+c>a:
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('TRIANGULO RETANGULO')
    elif a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < b**2 + c**2 or b**2 < a**2 + c**2 or c**2 < a**2 + b**2:
        print('TRIANGULO ACUTANGULO')
    if a==b==c:
        print('TRIANGULO EQUILATERO')
    elif a==b or b==c or c==a:
        print('TRIANGULO ISOsCELES')
    else:
        print('TRIANGULO ESCALENO')
else:
    print('NAO FORMA TRIANGULO')