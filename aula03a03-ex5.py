def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Lê um número do usuário
try:
    n = int(input("Digite quantos termos da sequência de Fibonacci deseja ver: "))
    if n <= 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        print(f"Sequência de Fibonacci com {n} termos:")
        fibonacci(n)
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
