hi, mi, hf, mf = [float(i) for i in input().split()]
mti = hi*60 + mi
mtf = hf*60 + mf
if hi < hf:
    mt = mtf-mti
    r = mt // 60
elif hi == hf:
    mt = mtf - mti
    r=24
else:
    mt = mti - mtf
    r = mt//60
s = mt - (mt//60)*60
print(f'O JOGO DUROU {r:.0f} HORA(S) E {s:.0f} MINUTO(S)')
