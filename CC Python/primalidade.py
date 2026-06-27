## primo: número divisivel somente por um e ele mesmo
numero = int(input("Digite um número:"))
divisor = 2
stop = True

while stop:
    if (numero % divisor) == 0:
        stop = False
    else:
        divisor = divisor + 1

if divisor == numero:
    print("primo")

else:
    print("não primo")