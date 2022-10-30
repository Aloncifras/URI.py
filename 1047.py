hi, mi, hf, mf = [int(i) for i in input().split()]
if hi < hf:
    if mi <= mf:
        tempo = (hf - hi, mf-mi)
    else:
        tempo = (hf-hi-1, 60-(mi-mf))
elif hf == hi:
    if mi == mf:
        tempo = (24, 0)
    elif mi < mf:
        tempo = (0, mf - mi)
    else:
        tempo = (23, 60-(mi-mf))
else:
    if mi <= mf:
        tempo = (24-(hi-hf), mf-mi)
    else:
        tempo = (24 - (hi - hf + 1), 60 - (mi - mf))
print(f'O JOGO DUROU {tempo[0]} HORA(S) E {tempo[1]} MINUTO(S)')