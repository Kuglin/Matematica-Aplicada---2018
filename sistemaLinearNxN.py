from sympy import *

variaveis =[]
equacoes = []
solucao = None

tam_matriz = int(input("Digite o tamanho da matriz: "))

for i in range(tam_matriz):

    simbolo = input("Digite o simbolo da variavel: ")

    codigo_string = "simbolo = symbols(simbolo)"
    exec(codigo_string)
    
    variaveis.append(simbolo)
    
for i in range(tam_matriz):

    equacao = input("Digite a equação: ")
    equacoes.append(equacao)

print("Variaveis: ", variaveis)
print()
print("equações: ", equacoes)
print()
solucao = solve(equacoes,variaveis)
print("Solução: ",solucao)