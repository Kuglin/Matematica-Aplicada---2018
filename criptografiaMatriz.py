from numpy import *					
from numpy.linalg import *					
import math					
					
chave_1= [2,1]					
chave_2= [1,3]					
					
matriz_cv = [chave_1,chave_2]					
matriz_cv_inv = inv(matriz_cv)					
					
texto_crp_1= [318,335,342,311,291,313,301,331,339,289,303,297,330,304,577,308,307,315,335,327,315,319,300,309,336,321]					
texto_crp_2= [449,430,446,448,398,394,398,443,442,382,394,386,445,437,566,449,396,395,420,401,420,417,425,432,453,413]					
					
texto_crp = [texto_crp_1,texto_crp_2]					
					
mult = (matmul(matriz_cv_inv, texto_crp))					
					
texto = [[],[]]					
					
					
for i in mult[0]:					
    texto[0].append(chr(math.ceil(float(str(i)[0:10]))))					
					
for i in mult[1]:					
    texto[1].append(chr(math.ceil(float(str(i)[0:10]))))					
					
for i in texto[0]:					
    print(i , end="")					
    print()					
for i in texto[1]:					
    print(i , end="")					
    print()