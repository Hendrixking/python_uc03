import time

def tabuada():
    n = int(input("Digite um número para ver a tabuada: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        time.sleep(0.3)

def dizer_ola():
    nome = input("Qual o seu nome? ")
    print(f"Olá, {nome}! Seja bem-vindo!")

def mostrar_quadrado():
    n = int(input("Digite um número: "))
    print(f"O quadrado de {n} é {n ** 2}")

interacoes = 0

while True:
    print("\n=== MENU ===")
    print("1. Ver tabuada")
    print("2. Dizer olá")
    print("3. Mostrar número ao quadrado")
    print("Digite 'sair' para encerrar.")
    
    escolha = input("Escolha uma opção: ").strip().lower()
    
    if escolha == 'sair':
        break
    elif escolha == '1':
        tabuada()
        interacoes += 1
    elif escolha == '2':
        dizer_ola()
        interacoes += 1
    elif escolha == '3':
        mostrar_quadrado()
        interacoes += 1
    else:
        print("Opção inválida. Tente novamente.")

print(f"\nVocê interagiu com o programa {interacoes} vezes. Até logo!")



