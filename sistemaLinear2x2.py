import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.ticker as ticker
import os

def verificar(a1,b1,c1,a2,b2,c2):

    if (a1*b2) - (b1*a2):
        
        pontos = []

        y1 = c1/b1
        x1 = c1/a1

        y2 = c2/b2
        x2 = c2/a2

        pontos.append([x1,0])
        pontos.append([0,y1])

        pontos2 = []
        pontos2.append([x2,0])
        pontos2.append([0,y2])

        lista = [[a1,b1],[a2,b2]]
        A = np.array(lista)
        B = np.array([c1,c2])
        X = np.linalg.solve(A,B)
        return X

        
    else: 
            
        cor1 = None
        cor2 = None

        cor1 = ((0,c1/b1), (c1/a1,0))
        cor2 = ((0,c2/b2), (c2/a2,0))

        if cor1 == cor2:
            lista = [a1,b1,c1]
            menor = min(lista)
            if menor<0:
                menor = -1*menor 

            if round(menor) == menor:
                for i in range(int(menor),1,-1):
                    if a1%i == 0 and b1%i == 0 and c1%i == 0:
                        a1 =  a1/i
                        b1 = b1/i 
                        c1 = c1/i 
                        break
                return [a1,b1,c1]
            return [a1,b1,c1]

        else:
            return [1]   

def dar_espaco(numero_linhas=100):

    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('\n'*numero_linhas)

def encontrar(x,y,x2,y2):

    a = ((y2-y)/(x2-x))
    b = (y - (x*a))

    return [a,b]

def fazer_desenho(x,y,x2=None,y2=None,s=None):
    fig, ax = plt.subplots()
    ax.plot(x,y, color="g")
    ax.plot(x2,y2, color="r")
    vx = (np.arange(s-10,s+11,1.0))
    ax.set_title("A", fontweight= "bold")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    
    ax.set_xticks(vx)

    ax.grid(True, linestyle='--')
    ax.tick_params(labelcolor="b", labelsize='medium', width=3)
    plt.show()


print("aaa")

if __name__ == "__main__":

    exe = True
    while exe:
        
        trava = input("Pressione Enter para continuar ...")
        dar_espaco()
        print("1 Sistema linear")
        print("2 Grafica")
        print("3 Sair")
        print()
        
        opcao = int(input("Digite a opção desejada: "))
    
        if opcao == 3:
            dar_espaco()
            exe = False

        elif opcao == 1:
            print("ax + by = c")
            print()
            a1= float(input("Digite o valor de a1: "))
            b1= float(input("Digite o valor de b1: "))
            c1= float(input("Digite o valor de c1: "))
            print("-" * 30)
            a2= float(input("Digite o valor de a2: "))
            b2= float(input("Digite o valor de b2: "))
            c2= float(input("Digite o valor de c2: "))
            print()


            solucao = verificar(a1,b1,c1,a2,b2,c2)
            if len(solucao) == 2:
                
                x = (np.arange(solucao[0]-10,solucao[0]+10,0.1))
                y = (c1 - (x*a1))/b1

                x2 = (np.arange(solucao[0]-10,solucao[0]+10,0.1))
                y2 = (c2 - (x2*a2))/b2 
                fazer_desenho(x,y,x2,y2,solucao[0])

                print("(" + str(solucao[0]) + ";" + str(solucao[1]) + ")")
                

            elif len(solucao) == 3:

                a1 = solucao[0]
                b1 = solucao[1]
                c1 = solucao[2]

                if a1 < 0:
                    print("x,(" + str(c1) + " +" + str(a1*(-1)) + "x)/" + str(b1))
                else:
                    print("x,(" + str(c1) + " -" + str(a1) + "x)/" + str(b1))

                x = (np.arange(-10,11,0.1))
                y = (c1 - (x*a1))/b1

                x2 = (np.arange(-10,11,0.1))
                y2 = (c2 - (x2*a2))/b2 
                    
                fazer_desenho(x,y,x2,y2,0)

            else:
                print("Impossível")

                x = (np.arange(-10,11,0.1))
                y = (c1 - (x*a1))/b1

                x2 = (np.arange(-10,11,0.1))
                y2 = (c2 - (x2*a2))/b2 
                    
                fazer_desenho(x,y,x2,y2,0)
                    
        elif opcao == 2:
            
            print()
            x1= float(input("Digite o valor de x1:  "))
            y1= float(input("Digite o valor de y1:  "))
            print("-" * 30)
            x2= float(input("Digite o valor de x2: "))
            y2= float(input("Digite o valor de y2: "))
            print()

            cordenada = encontrar(x1,y1,x2,y2)
    
            print("Equação: " + str(cordenada[0]*-1) + " + y = " + str(cordenada[1]))
            print()
            print("Equação: " + str(cordenada[0]) + " - y = " + str(cordenada[1]*-1))
            
        else:
            print("Opção inválida ...")
