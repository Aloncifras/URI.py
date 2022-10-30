a, b = [int(i) for i in input().split()]
if a == b:
    r=24
elif a > b:
    r=24-a+b
elif a < b:
    r=b-a
print(f'O JOGO DUROU {r} HORA(S)')