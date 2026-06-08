import pygame
import sys
import numpy as np

Xwin = 50  # Tamanho da matriz (50x50)
Ywin = 50

# Cores
BRANCO = (255, 255, 255)
AZUL   = (0, 0, 255)

M = np.zeros((Xwin, Ywin))

def desenhaMatriz(M):
    for i in range(0, Xwin):
        for j in range(0, Ywin):
            if M[i, j] == 1:
                # Desenha o quadrado/círculo preenchendo o bloco de 10x10 pixels
                pygame.draw.rect(screen, AZUL, (10 * i, 10 * j, 9, 9))

def inicial(M):
    # Vamos criar uma forma clássica que se move sozinha (Glider/Planador)
    # para você ver o jogo funcionando logo de início
    M[1, 2] = 1
    M[2, 3] = 1
    M[3, 1] = 1
    M[3, 2] = 1
    M[3, 3] = 1

def iteracao(M):
    Mnew = np.zeros((Xwin, Ywin))
    
    for i in range(Xwin):
        for j in range(Ywin):
            # Conta os 8 vizinhos ao redor da célula (i, j)
            # O operador % garante que a borda dê a volta na tela (mapa infinito/toroidal)
            vizinhos_vivos = int(
                M[(i-1)%Xwin, (j-1)%Ywin] + M[(i-1)%Xwin, j] + M[(i-1)%Xwin, (j+1)%Ywin] +
                M[i, (j-1)%Ywin]                             + M[i, (j+1)%Ywin] +
                M[(i+1)%Xwin, (j-1)%Ywin] + M[(i+1)%Xwin, j] + M[(i+1)%Xwin, (j+1)%Ywin]
            )
            
            # Aplica as regras do Jogo da Vida
            if M[i, j] == 1:
                if vizinhos_vivos == 2 or vizinhos_vivos == 3:
                    Mnew[i, j] = 1.0  # Sobrevive
                # Se for < 2 ou > 3, Mnew continua 0 (Morre por solidão ou superpopulação)
            else:
                if vizinhos_vivos == 3:
                    Mnew[i, j] = 1.0  # Renasce
                    
    return Mnew

# Inicializa o Pygame
pygame.init()       
screen = pygame.display.set_mode((10 * Xwin, 10 * Ywin))
pygame.display.set_caption("Jogo da Vida de Conway")
clock = pygame.time.Clock() # Para controlar a velocidade

inicial(M)

jogando = False  # Começa pausado para você poder clicar/ver o padrão inicial

while True:
    screen.fill(BRANCO) 
    desenhaMatriz(M)    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Clique do mouse: Adiciona/Remove células manualmente para testar
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = x // 10, y // 10
            # Inverte o estado da célula clicada
            M[grid_x, grid_y] = 1.0 if M[grid_x, grid_y] == 0.0 else 0.0

        # Barra de Espaço: Pausa ou roda o jogo automaticamente
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jogando = not jogando
                print(f"Jogo rodando: {jogando}")

    # Se o jogo não estiver pausado, ele evolui a cada frame
    if jogando:
        M = iteracao(M)
        clock.tick(10) # Limita a 10 gerações por segundo para dar tempo de enxergar
        
    pygame.display.flip()