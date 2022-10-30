a=0
while a != 25:
    a, b, c, d = [int(i) for i in input().split()]
    if a == c:
        r=24
    elif a < c and b > d:
        r=c-a-1
    elif a > c:
        r = (24-a)+c
    elif a < c:
        r=c-a
    if b == d:
        s=0
    elif a > c and d < b:
        r=24-a+c-1
        s=60-b+d
    elif b > d:
        s=60-b+d
    elif b < d:
        s=d-b
    print(f'O JOGO DUROU {r} HORA(S) E {s} MINUTO(S)')

'''
7 8 9 10

O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

7 7 7 7

O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

7 10 8 9

O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)

20 10 16 50

O JOGO DUROU 20 HORA(S) E 40 MINUTO(S)

20 50 16 10

O JOGO DUROU 19 HORA(S) E 20 MINUTO(S)



'''