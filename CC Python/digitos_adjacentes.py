Numero = input("Digite um numero inteiro:")
numero = int(Numero)
casas = len(Numero)
anterior = 0
resto = numero

if casas == 1:
    casas = 0
    anterior = -1

while casas != 0:
    if anterior == numero:
        casas = 0

    else: 
        anterior = numero
        numero = resto //10**(casas - 1)
        resto  = resto % 10**(casas - 1)
        casas = casas - 1
     
if anterior == numero:
    print("sim")

else:
    print("não")