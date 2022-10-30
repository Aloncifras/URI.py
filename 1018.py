D = int(input(''))
#Legenda D=Dinheiro a sacar; n(valor)= nota de "valor" reais
n100 = int(D//100) #Divisao inteira por 100 dará quantas notas de 100 cabe no Dinheiro
n50 = int((D-n100*100)//50) #ao fazer "D-n100*100" pego o dinheiro inicial e retiro a quantidade de dinheiro já sacado em notas de 100
n20 = int((D-(n100*100+n50*50))//20) #analogamente nas notas de vinte a diante...
n10 = int((D-(n100*100+n50*50+n20*20))//10)
n5 = int((D-(n100*100+n50*50+n20*20+n10*10))//5)
n2 = int((D-(n100*100+n50*50+n20*20+n10*10+n5*5))//2)
n1 = int((D-(n100*100+n50*50+n20*20+n10*10+n5*5+n2*2))//1)
print('{:.0f}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'.format(D,n100, n50, n20, n10, n5, n2, n1))
