from math import trunc
D = float(input("Digite o valor a sacar: "))
#Legenda D=Dinheiro a sacar; n(valor)= nota de "valor" reais; m(valor)=moeda de "valor" reais
n100 = int(D//100) #Divisao inteira por 100 dará quantas notas de 100 cabe no Dinheiro
n50 = int((D-n100*100)//50) #ao fazer "D-n100*100" pego o dinheiro inicial e retiro a quantidade de dinheiro já sacado em notas de 100
n20 = int((D-(n100*100+n50*50))//20) #analogamente nas notas de vinte a diante...
n10 = int((D-(n100*100+n50*50+n20*20))//10)
n5 = int((D-(n100*100+n50*50+n20*20+n10*10))//5)
n2 = int((D-(n100*100+n50*50+n20*20+n10*10+n5*5))//2)
m100 = int((D-(n100*100+n50*50+n20*20+n10*10+n5*5+n2*2))//1) #moedas de 1 real
m = float(round(D-trunc(D),2)) #pegando o Dineiro e retirando a parte inteira para sobrar só os centavos #gambiarra pq 90.01-90!=0.01 COMPUTADOR DROGADO!
#Ex: print(90.1-90)
m50 = int(round(m / 0.5)) #ao pegar os centavos fazer a divisão inteira por 0.50 tenho quantas moedas preciso de 50 (sempre 0 ou 1)
m25 = int(round(m - (m50*0.5), 2) / 0.25) # ao pegar os centavos e retirar ou 0 ou 50 cents que já foram sacados sobre somente o restante"
m10 = int(round(m - (m50*0.5+m25*0.25), 2) / 0.1) # analogamente a cima...
m5 = int(round(m - (m50*0.5 + m25*0.25 + m10*0.1), 2) / 0.05)
m1 = int(round(m - (m50*0.5 + m25*0.25 + m10*0.1 + m5*0.05), 2) / 0.01)
print('NOTAS:\n'
    '{} nota(s) de R$ 100.00\n'
    '{} nota(s) de R$ 50.00\n'
    '{} nota(s) de R$ 20.00\n'
    '{} nota(s) de R$ 10.00\n'
    '{} nota(s) de R$ 5.00\n'
    '{} nota(s) de R$ 2.00'
    '\nMOEDAS:\n'
    '{} moeda(s) de R$ 1.00\n'
    '{} moeda(s) de R$ 0.50\n'
    '{} moeda(s) de R$ 0.25\n'
    '{} moeda(s) de R$ 0.10\n'
    '{} moeda(s) de R$ 0.05\n'
    '{} moeda(s) de R$ 0.01'
        .format(n100, n50, n20, n10, n5, n2, m100, m50, m25, m10, m5, m1))
##Funcionou em todos os exemplos explicitos, mas está com 5% de erro ainda provavelmente devido a quantidade de arredondamentos necessarios por subtrações simples darem errado!