def usuario_escolhe_jogada(n, m):

    ### Docstring
    ###
    ### Recebe dois parâmetros (n e m), solicita ao usuário a jogada e verifica a válidade da jogada,
    ### se a jogada for válida retorna ela, caso contrário solicita uma nova entrada

    ### n: número inicial de peças
    ### m: número máximo de peças que pode ser retiradas por jogada
    ### jogada: numero de peças que o jogador deseja retirar
    ### validade: verifica a validade da jogada

    validade = True

    while validade:
        jogada = int(input("Quantas peças você vai tirar?"))

        if jogada > m or jogada <= 0:
            print()
            print("Jogada inválida! Tente de novo")

        else: 
            validade = False
    
        print()
    
    if jogada != 1:
        print("Você tirou", jogada, "peças do tabuleiro")

    else:
        print("Você tirou uma peça do tabuleiro")

    return jogada

def computador_escolhe_jogada(n, m):

    ### Docstring
    ###
    ### Recebe dois parâmetros (n e m), funciona de forma isolada e retorna a jogada do computador (jogada ótima)
    ### A jogada ótima consiste em deixar (m + 1) peças ao oponente

    ### n: número inicial de peças
    ### m: número máximo de peças que pode ser retiradas por jogada
    ### jogadaC: numero de peças retiradas pelo computador
    ### m2: usada para operar no lugar de m (evita alterar o valor de m)

    jogadaC = 0
    m2 = m

    while m2 > 0:
        if (n - m2) % (m + 1) == 0:
            jogadaC = m2
            break

        else:
            m2 -= 1

    if m2 == 0:
        jogadaC = m

    n -= jogadaC

    if jogadaC != 1:
        print("O computador tirou", jogadaC, "peças do tabuleiro")

    else:
        print("O computador tirou uma peça do tabuleiro")

    return jogadaC
    
def partida():

    ### Docstring
    ### 
    ### Não recebe nenhum parâmetro, solicita ao usuário os valores de n e m e inicia a partida, define quem começa,
    ### deve alternar as jogadas entre o computador e o usuário, define quem ganhou e informa quem é o vencedor
    ### Se n é multiplo de (m + 1) o jogador inicia a partida, caso contrário o computador inicia

    ### n: numero inicial de peças
    ### m: número máximo de peças que pode ser retirada por jogada
    ### resultado: resultado da partida, é a variável que a função retorna e dever ser = "comp" caso o computador ganhe caso contraário deve se = "jog"
    ### loop: define quala a ordem das jogadas entre jogador e usuário

    n = int(input("Quantas peças?"))
    m = int(input("Quantas peças por jogada?"))
    resultado = 0
    loop = 0

    if n % (m + 1) == 0:
        print()
        print("Você começa!")

        x = usuario_escolhe_jogada(n, m)

        if n - x == 1:
            print("Sobrou somente uma peça no tabuleiro")

        else:
            print("Sobraram", n - x, "peças no tabuleiro")

        loop = 1
        n -= x

    else:
        print()
        print("Computador começa!")

        z = computador_escolhe_jogada(n, m)

        if n - z == 1:
            print("Sobrou somente uma peça no tabuleiro")

        else:
            print("Sobraram", n - z, "peças no tabuleiro")

        loop = 2
        n -= z

    while resultado == 0:

        if loop == 1:
            if n == 0:
                print("Fim do jogo! Você venceu!")
                resultado = "jog"

            else:
                y = computador_escolhe_jogada(n, m)
                n -= y
                
                if n == 0:
                    print("Fim de jogo! O computador ganhou!")
                    resultado = "comp"

                else:
                    print("Restam", n, "peças no tabuleiro")
                    w = usuario_escolhe_jogada(n, m)
                    n -= w
                    print()
                    print("Restam", n, "peças no tabuleiro")

        else:
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                resultado = "comp"

            else:
                a = usuario_escolhe_jogada(n, m)
                n -= a
                
                if n == 0:
                    print("Fim de jogo! Você venceu!")
                    resultado = "jog"

                else:
                    print("Restam", n, "peças no tabuleiro")
                    b = computador_escolhe_jogada(n, m)
                    n -= b
                    print()
                    print("Restam", n, "peças no tabuleiro")

    return resultado

def campeonato():

    ### Docstring
    ###
    ### Chama a função partida três vezes, define o vencedor do campeonato e informa o placar

    ### Result(1,2,3): armazena o resultado da partida correspondente
    ### pJog: informa a pontuação do jogador
    ### pComp: informa a pontuação do jogador 

    result1 = "indef"
    result2 = "indef"
    result3 = "indef"
    pJog = 0
    pComp = 0

    # Primeira rodada #
    print()
    print("**** Rodada 1 ****")
    result1 = partida()

    # Segunda rodada #
    print()
    print("**** Rodada 2 ****")
    result2 = partida()

    # Terceira rodada #
    print()
    print("**** Rodada 3 ****")
    result3 = partida()

    # Processamento da pontuação #
    if result1 == "comp":
        pComp += 1
    else:
        pJog += 1
    
    if result2 == "comp":
        pComp += 1
    else:
        pJog += 1

    if result3 == "comp":
        pComp += 1
    else:
        pJog += 1

    # Finalização #
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você",pJog,"X",pComp,"Computador")
    
def main():

    ### Docstring
    ###
    ### Inicia a partida, solicita ao jogador a modalidade (campeonato ou partida).

    ### Verificador: verifica se o usuário digitou uma opção válida
    ### modelo: variavel que identifica se o jogo será um campeonato ou uma partida

    Verificador = True

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida")
    print("2 - para jogar um campeonato")
    print()

    while Verificador:
        modelo = int(input())

        if modelo == 1:
            Verificador = False

        elif modelo == 2:
            Verificador = False   

    if modelo == 1:
        print("Você escolheu partida!")
        partida()
    
    else:
        print("Você escolheu campeonato!")
        campeonato()

main()