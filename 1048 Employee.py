si=float(input())
if si <= 400:
    p=1.15
elif si <= 800:
    p=1.12
elif si <= 1200:
    p=1.1
elif si <= 2000:
    p=1.07
else:
    p=1.04
sf =p*si
print(f'''Novo salario: {sf:.2f}
Reajuste ganho: {sf-si:.2f}
Em percentual: {(p-1)*100:.0f} %''')