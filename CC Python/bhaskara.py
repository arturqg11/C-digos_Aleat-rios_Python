import math

a = float(input("Digite um valor inteiro para a:"))
b = float(input("Digite um valor inteiro para b:"))
c = float(input("Digite um valor inteiro para c:"))

Delta = (b**2) - (4*a*c)

if Delta < 0:
    print("esta equação não possui raízes reais")

if Delta == 0:
    Raizes = (-(b) + math.sqrt(Delta))/2*a
    print("a raiz desta equação é",Raizes)

if Delta > 0:
    Raiz1 = (-(b) + math.sqrt(Delta))/2*a
    Raiz2 = (-(b) - math.sqrt(Delta))/2*a
    
    if Raiz1 > Raiz2:
         print("as raízes da equação são",Raiz2,"e",Raiz1)
    
    else:
        print("as raízes da equação são",Raiz1,"e",Raiz2)