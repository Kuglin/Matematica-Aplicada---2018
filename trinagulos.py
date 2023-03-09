import math
a= float(input("Digite a medida de a :"))
b= float(input("Digite a medida de b :"))
c= float(input("Digite a medida de c :"))
print("1 para em graus")
print("2 para em radianos")
opcao=int(input("escolha em que medida quer dar o valor dos angulos: "))
if opcao==2:
    A= float(input("Digite a medida de A :"))
    B= float(input("Digite a medida de B :"))
    C= float(input("Digite a medida de C :"))
else:
    A= math.radians(float(input("Digite a medida de A :")))
    B= math.radians(float(input("Digite a medida de B :")))
    C= math.radians(float(input("Digite a medida de C :")))
if sum([A,B,C])>math.pi:
        print("Angulos foram dados incoretamente")
        exit(0)
while a<=0 or b<=0 or c<=0 or A<=0 or B<=0 or C<=0:
    if (a>0 and C>0 and A>0) and c<=0:
        c=a*math.sin(C)/math.sin(A)
    if (A>0 and C>0) and B<=0:
        B=math.pi-A-C
    if a>0 and B>0 and A>0 and b<=0:
        b=a*math.sin(B)/math.sin(A)
    if B>0 and C>0 and A<=0:
        A=math.pi-B-C
    if A>0 and B>0 and C<=0:
        C=math.pi-A-B
    if b>0 and A>0 and B>0 and a<=0:
        a=b*math.sin(A)/math.sin(B)
    if b>0 and C>0 and B>0 and c<=0:
        c=b*math.sin(C)/math.sin(B)
    if a<=0 and c>0 and A>0 and B>0:
        a=c*math.sin(A)/math.sin(math.pi-A-B)
    if b<=0 and c>0 and B>0 and A>0:
        b=c*math.sin(B)/math.sin(math.pi-A-B)
    if b<=0 and c>0 and B>0 and C>0:
        b=c*math.sin(B)/math.sin(C)
    if B<=0 and b>0 and A>0 and a>0:
        B=math.asin(b*math.sin(A)/a)
    if c<=0 and a>0 and b>0 and C>0:
        c=sqrt(pow(a, 2)+pow(b, 2)-2*a*b*math.cos(C))
    if C<=0 and c>0 and A>0 and a>0:
        C=math.asin(c*math.sin(A)/a)
    if a<=0 and b>0 and c>0 and A>0:
        a=sqrt(pow(b, 2)+pow(c, 2)-2*b*c*math.cos(A))
    if B<=0 and a>0 and c>0 and b>0:
        B=math.acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
    if A<=0 and a>0 and B>0 and b>0:
        A=math.asin(a*math.sin(B)/b)
    if b<=0 and a>0 and c>0 and a>0 and c>0 and B>0:
        b=sqrt(pow(a, 2)+pow(c, 2)-2*a*c*math.cos(B))
    if A<=0 and b>0 and c>0 and a>0:
        A=math.acos((pow(b, 2)+pow(c, 2)-pow(a, 2))/(2*b*c))
    if C<=0 and c>0 and B>0 and b>0:
        C=math.asin(c*math.sin(B)/b)
    if a<=0 and c>0 and A>0 and c>0:
        a=c*math.sin(A)/math.sin(C)
    if A<=0 and a>0 and C>0 and c>0:
        A=math.asin(a*math.sin(C)/c)
    if B<=0 and b>0 and C>0 and c>0:
        B=math.asin(b*math.sin(C)/c)
    if C<=0 and a>0 and b>0 and c>0:
        C=math.acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))

print("a = " + str(a) + " cm")
print("b = " + str(b) + " cm")
print("c = " + str(c) + " cm")
print("A = " + str(A) + " radianos ou " + str(math.degrees(A)) + " graus")
print("B = " + str(B) + " radianos ou " + str(math.degrees(B)) + " graus")
print("C = " + str(C) + " radianos ou " + str(math.degrees(C)) + " graus")