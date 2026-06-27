import math

xA = int(input("Digite um número inteiro:"))
yA = int(input("Digite um número inteiro:"))
xB = int(input("Digite um número inteiro:"))
yB = int(input("Digite um número inteiro:"))

distancia = math.sqrt((xA - xB)**2 + (yA - yB)**2)

if distancia >= 10:
    print("longe")

else:
    print("perto")