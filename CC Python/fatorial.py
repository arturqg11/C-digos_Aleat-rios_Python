## Receber um natural n e devolver seu fatoria
## Fatorial de 5: 5! =  5 * 4 * 3 * 2 * 1
## Generalização n! = n * (n-1) * (n - 2) * ... * 1

numero = int(input("Digite um número natural:"))

numeroF = 1

if numero == 0:
    print(1)

else:

    while numero != 1:
        numeroF = numeroF * numero
        numero = numero - 1
    
    print(numeroF)