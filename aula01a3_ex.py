# Exercício 6: Verifique se um usuário pode votar (idade >= 18).

def verificar_idd(idade):
 if idade >= 18:
    print("!!!PODE VOTAR!!!: ")
 else:
    print("!!!NÃO PODE VOTAR!!!: ")

idd = float(input("DIGITE SUA IDADE: "))
verificar_idd(idd)


# Exercício 10: Peça ao usuário um número e exiba 'Alto' se for maior que 100 e 'Baixo' se for menor.

def verificar_num(numero):

 if numero >= 100:
    print("!!!MAIOR QUE 100!!!:  ")
 else:
    print ("!!!MENOR QUE 100!!!: ")

num = int(input("DIGITE UM NUMERO: "))
verificar_num(num)

# Exercício 8: Verifique se uma senha digitada corresponde a '1234'.

def verificar_sen(senha):

 if senha == 1234:
    print("!!!SENHA CORRETA!!!: ")
 else:
    print("!!!!SENHA ERRADA!!!!: ")

sen = int(input(" DIGITE SUA SENHA: "))
verificar_sen(sen)

#Exercício 9: Verifique se um número está entre 10 e 50.

def verificar_num(numero):

 if 10 <= numero <= 50:
    print("!!!ESTA ENTRE O 10 E 50!!: ")
 else:
    print("!!!!NÃO ESTA ENTRE O 10 E 50!!!: ")

 num = int(input(" DIGITE UM NUMERO: "))
 verificar_num(num)

#Exercício 2: Peça dois números e exiba o maior.
 
numero1 = int(input(" DIGITE UM NUMERO: "))
numero2 = int(input(" DIGITE UM NUMERO: "))

def verificar_maior(numero1, numero2):
 if numero1 >= numero2:
    print(f"{numero1}: É MAIOR")
 else:
    print(f"{numero2}: É MAIOR")

verificar_maior(numero1, numero2)


#Exercício 5: Peça três números e exiba o maior.

numero1 = int(input(" DIGITE UM NUMERO: "))
numero2 = int(input(" DIGITE UM NUMERO: "))
numero3 = int(input(" DIGITE UM NUMERO: "))

def verificar_maior(numero1, numero2, numero3): 

 maior = max(numero1, numero2, numero3)
 print(f"{maior}: É MAIOR")

 verificar_maior(numero1, numero2, numero3)


#Exercício 5: Peça três números e exiba o maior.

numero1 = int(input(" DIGITE UM NUMERO: "))
numero2 = int(input(" DIGITE UM NUMERO: "))
numero3 = int(input(" DIGITE UM NUMERO: "))

def verificar_maior(numero1, numero2, numero3): 

 maior = max(numero1, numero2, numero3)
 print(f"{maior}: É MAIOR")

 verificar_maior(numero1, numero2, numero3)
