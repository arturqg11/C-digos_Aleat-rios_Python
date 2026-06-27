def fatorial(numero):

    numeroF = 1

    if numero == 0:
        numeroF = 1

    else:

        while numero != 1:
            numeroF = numeroF * numero
            numero = numero - 1
    
    return numeroF

N = int(input("Digite o valor de n:"))
K = int(input("Digite o valor de k:"))

n = fatorial(N)
k = fatorial(K)
nk = fatorial(N - K)

binomio = n/(k * nk)

print(int(binomio))