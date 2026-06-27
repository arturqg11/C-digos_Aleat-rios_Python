l = int(input("Digite a largura:"))
h = int(input("Digite a altura"))
linha = 0

while linha < h:
    coluna = 0
    
    while coluna < l:
        print("#", end = "")
        coluna += 1

    print()
    linha += 1