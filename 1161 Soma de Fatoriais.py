from math import factorial
while True:
    try:
        x,y = [int(i) for i in input().split()]
        print(factorial(x)+factorial(y))
    except EOFError:
        break
