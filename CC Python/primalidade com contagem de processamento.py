## primo: número divisivel somente por um e ele mesmo
import time

numero = int(input("Digite um número:"))
divisor = 2
stop = True

inicio =  time.time()

while stop:
    if (numero % divisor) == 0:
        stop = False
    else:
        divisor = divisor + 1

if divisor == numero:
    print("primo")

else:
    print("não primo")

for i in range(1000000):
    pass

fim = time.time()
tempo_gasto = fim - inicio
print(f"tempo gasto: {tempo_gasto: .4f} segundos")