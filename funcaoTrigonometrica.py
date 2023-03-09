import matplotlib.pyplot as plt
import numpy

def funcao_seno(a,b,c,d,x):
    y = a*numpy.sin(b*x+c)+d
    return y

def funcao_cosseno(a,b,c,d,x):
    y = a*numpy.cos(b*x+c)+d
    return y

if __name__=="__main__":
    a= float(input("digite a: "))
    b= float(input("digite b: "))
    c= float(input("digite c: "))
    d= float(input("digite d: "))

    print("sin para seno")
    print("cos para cosseno")
    print("tan para tangente")
    opcao=input("digite a opção que voce quer: ")
    if opcao=="cos":
        p = 2*((2*numpy.pi)/b)
        x = numpy.arange(0.0,p,0.01)
        y1 = funcao_cosseno(a,b,c,d,x)
        fig, ax = plt.subplots()
        ax.plot(x,y1)

        periodo="periodo: " + str(p/2) + "  /  "
        imagem = [d-a,d+a]
        imagem.sort
        amplitude = (imagem[1]-imagem[0])/2
        imagem = "imagem: " + str(imagem) + "  /  "
        amplitude= "amplitude:" + str(amplitude)

    if opcao=="sin":
        p = 2*((2*numpy.pi)/b)
        x = numpy.arange(0.0,p,0.01)
        y1 = funcao_seno(a,b,c,d,x)
        fig, ax = plt.subplots()
        ax.plot(x,y1)

        periodo="periodo: " + str(p/2)
        imagem = [d-a,d+a]
        imagem.sort
        amplitude = (imagem[1]-imagem[0])/2
        imagem = "imagem: " + str(imagem) + "  /  "
        amplitude= "amplitude:" + str(amplitude)

    if opcao=="tan":
        
        p = 2*((2*numpy.pi)/b)
        periodo="periodo: " + str(p/2) + "  /  "
        amplitude=""
        imagem=""

    plt.xlabel(periodo + imagem + amplitude)
    plt.show()