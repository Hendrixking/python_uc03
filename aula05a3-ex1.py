# Função -  manipulação de arquivos
# Criar uma função que crie e adicione um texto no arquivo

def criar_arquivo(nome_arquivo: str, conteudo: str):
  
    with open(nome_arquivo, 'w') as arquivo:
       arquivo.write(conteudo)
       print("Arquivo criado com secesso")

nome = input("Digite o nome do arquivo: ")
criar_arquivo(f'./src/arquivos/{nome}.txt',"este é um arquivo criado com python: ")


# Ler o arquivo 

def ler_arquivo(nome_arquivo: str):
  
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

nome = input("Digite o nome do arquivo: ")
print(ler_arquivo(f'./src/arquivos/{nome}.txt'))


# Adicionar conteudo

def adicionar_conteudo(nome_arquivo: str, conteudo: str):
  
    with open(nome_arquivo, 'a') as arquivo:
       arquivo.write('\n' + conteudo)
       print("Arquivo criado com secesso")

nome = input("informe o nome do arquivo: ")
conteudo = input("Digite o texto a ser adicionado:")
adicionar_conteudo(f'./src/arquivos/{nome}.txt',"este é um arquivo criado com python:")


# Remover arquivo

import os

def remover_arquivo(nome_arquivo: str):
  
   if os.path.exists(nome_arquivo):
    os.remove(nome_arquivo)
    print("Arquivo removido")

   else:
    print("Arquivo não encontrado")


nome = input("Informe o nome do arquivo que deseja remover: ")
remover_arquivo(f"./src/arquivos/{nome}.txt")

# Contar quantas linhas preenchidas possui no arquivo

def contar_linhas(nome_arquivo: str):
  
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readline())

nome = input("Informe o nome do arquivo: ")
print(contar_linhas(f'./src/arquivos/{nome}.txt'))

# Verificar se uma palavra existe no conteudo

def verificar_palavra(nome_arquivo: str, palavra: str) -> bool:
  
    with open(nome_arquivo, 'r') as arquivo:
        return palavra in arquivo.read()

nome = input("Informe a palavras do arquivo: ")
print(verificar_palavra(f'./src/arquivos/{nome}.txt','python'))


