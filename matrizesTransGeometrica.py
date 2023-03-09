import pygame

matrizes=[]

def listar_lista(lista):
    nova_lista=[]
    for i in lista:
        nova_lista.append(list(i))
    return nova_lista

def desenhar_linha(pontos,max_x):
    lista_pontos=listar_lista(pontos)
    for i in range(4):
        matrizes.append(list(listar_lista(lista_pontos)))
        for i in lista_pontos:
            i[0]+=max_x
    return matrizes

def desenhar_varias_linhas(pontos):
    max_x=descobrir_max(pontos,0)
    max_y=descobrir_max(pontos,1)
    lista_pontos=listar_lista(pontos)
    for i in range(4):
        desenhar_linha(lista_pontos,max_x)
        for i in lista_pontos:
            i[1]+=max_y


def descobrir_max(pontos,x_y):
    max=0
    for i in pontos:
        if i[x_y]>max:
            max=i[x_y]
    return max

def desenho_1():
    desenhar_varias_linhas(pontos)
    cor=255
    for i in matrizes:
        cor-=13
        pygame.draw.polygon(tela,(cor,0,0), i)
    for i in range(200):
        print()
    print("----------- Matriz 4x4 ----------")
    printar_4x4(15)

def printar_4x4(n_matriz):
    matriz_4x4=[]
    for i in matrizes[n_matriz]:
        matriz_4x4.append([(i[0]/tamanho_maior),(i[1]/tamanho_maior)])
    print("X:  ", end="")
    for i in matriz_4x4:
        print(i[0], "  ", end="")
    print("")
    print("Y:  ", end="")
    for i in matriz_4x4:
        print(i[1], "  ", end="")
    print("")

def desenho_2():
    desenhar_varias_linhas(pontos)
    valor_somado_x=descobrir_max(matrizes[0],0)
    valor_somado_y=descobrir_max(matrizes[0],1)
    for i in range(len(matrizes)):
        for y in range(len(matrizes[i])):
            if i%2!=0:
                matrizes[i][y][0]*=-1
                if i not in [3,7,11,15]:
                     matrizes[i][y][0]+=3*valor_somado_x
                else:
                    matrizes[i][y][0]+=7*valor_somado_x
            if i in [4,5,6,7]:
                matrizes[i][y][1]*=-1
                matrizes[i][y][1]+=3*valor_somado_y
            if i in [12,13,14,15]:
                matrizes[i][y][1]*=-1
                matrizes[i][y][1]+=7*valor_somado_y
    cor=255
    for i in matrizes:
        pygame.draw.polygon(tela,(0,cor,0), i)
        cor-=13
    for i in range(200):
        print()
    print("----------- Matriz 3x3 ----------")
    printar_4x4(10)
    print("----------- Matriz 3x4 ----------")
    printar_4x4(11)
    print("----------- Matriz 4x3 ----------")
    printar_4x4(14)
    print("----------- Matriz 4x4 ----------")
    printar_4x4(15)
         
def desenho_3():
    desenhar_varias_linhas(pontos)
    valor_somado_x=descobrir_max(matrizes[0],0)
    valor_somado_y=descobrir_max(matrizes[0],1)
    for i in range(len(matrizes)):
        valor_multiplicavel_x=((descobrir_valor_multiplicavel(i,0)+1)*2)-1
        valor_multiplicavel_y=((descobrir_valor_multiplicavel(i,1)+1)*2)-1
        for y in range(len(matrizes[i])):
            if i in [1,3,4,6,9,11,12,14]:
                matrizes[i][y][0]*=-1
                matrizes[i][y][1]*=-1
                matrizes[i][y][0]+=valor_somado_x*valor_multiplicavel_x
                matrizes[i][y][1]+=valor_somado_y*valor_multiplicavel_y
    cor=255
    for i in matrizes:
        pygame.draw.polygon(tela,(0,0,cor), i)
        cor-=13
    for i in range(200):
        print()
    print("----------- Matriz 3x4 ----------")
    printar_4x4(11)
    print("----------- Matriz 4x4 ----------")
    printar_4x4(15)

def descobrir_valor_multiplicavel(pos,x_y):
    if x_y==1:
        if pos<4:
            return 0
        elif pos<8:
            return 1
        elif pos<12:
            return 2
        else:
            return 3
    else:
        if pos in [0,4,8,12]:
            return 0
        elif pos in [1,5,9,12]:
            return 1
        elif pos in [2,6,10,14]:
            return 2
        else:
            return 3

def executar(num):
    if num==1:
        desenho_1()
    if num==2:
        desenho_2()
    if num==3:
        desenho_3()

pontos_x = input("Digite os pontos em X: ")
pontos_x = pontos_x.split(" ")
pontos_y = input("Digite os pontos em Y: ")
pontos_y = pontos_y.split(" ")
if len(pontos_x) != len(pontos_y):
    print("Erro")
    exit(0)

pontos =[]
for i in range(len(pontos_x)):
    pontos.append([float(pontos_x[i]),float(pontos_y[i])])

tela = pygame.display.set_mode((600, 600), 0, 32)
tela.fill((255,255,255))

pygame.init()

tamanho_x=150/descobrir_max(pontos,0)
tamanho_y=150/descobrir_max(pontos,1)

if tamanho_x<tamanho_y:
    tamanho_maior=tamanho_x
else:
    tamanho_maior=tamanho_y

for i in pontos:
    i[0]=i[0]*tamanho_maior
    i[1]=i[1]*tamanho_maior

num = 1

executar(num)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            matrizes=[]
            if num==3:
                num=1
                tela.fill((255,255,255))
                executar(num)
                pygame.display.update()
            else:
                num+=1
                tela.fill((255,255,255))
                executar(num)
                pygame.display.update()