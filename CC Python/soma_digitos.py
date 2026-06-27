numero = input("digite um número inteiro:")
casas = len(numero)
Numero = int(numero)
resto = Numero
soma = 0

while casas != 0:
    Numero = resto // 10**(casas - 1)
    soma = soma + Numero 
    resto = resto % 10**(casas - 1)
    casas = casas - 1

print(soma)