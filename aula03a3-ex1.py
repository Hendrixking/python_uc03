inicio= int(input("DIGITE UM NUMERO: "))
final= int(input(" DIGITE UM NUMERO: "))

def imprimir(inicio, final):  
    for numero in range(inicio, final+1):
        print(f"{numero}")

imprimir(inicio, final)