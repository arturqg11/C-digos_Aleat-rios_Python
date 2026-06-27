## ímpar é um 2k - 1, se i = 5 -> 1 3 5 7 9

quantidade = int(input("Digite um número natural:"))
cont = 1

while cont != quantidade:
    print(cont * 2 - 1)
    cont += 1

print(cont * 2 - 1)