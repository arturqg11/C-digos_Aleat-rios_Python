## Receber um natural n e devolver seu fatoria
## Fatorial de 5: 5! =  5 * 4 * 3 * 2 * 1
## Generalização n! = n * (n-1) * (n - 2) * ... * 1

import time

numero = int(input("Digite um número natural:"))

numeroF = 1

inicio = time.time()

if numero == 0:
    print(1)

else:

    while numero != 1:
        numeroF = numeroF * numero
        numero = numero - 1
    
    print(numeroF)

for i in range(1000000):
    pass

fim = time.time()
tempo_gasto = fim - inicio
print(f"tempo gasto: {tempo_gasto: .4f} segundos")