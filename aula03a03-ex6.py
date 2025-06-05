import time

def tabuada(numero):
    for i in range(1, 11):
        r = numero * i
        print(f"A TABUADA DE {numero} x {i} = {r}")
        time.sleep(0.5) 

n = int(input("DIGITE UM NÚMERO: "))
tabuada(n)
