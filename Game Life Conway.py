import pygame
import sys
import numpy as np

Xwin = 50  
Ywin = 50

BRANCO = (255, 255, 255)
AZUL   = (0, 0, 255)

M = np.zeros((Xwin, Ywin))

def desenhaMatriz(M):
    for i in range(0, Xwin):
        for j in range(0, Ywin):
            if M[i, j] == 1:
                
                pygame.draw.rect(screen, AZUL, (10 * i, 10 * j, 9, 9))

def inicial(M):
    M[1, 2] = 1
    M[2, 3] = 1
    M[3, 1] = 1
    M[3, 2] = 1
    M[3, 3] = 1

def iteracao(M):
    Mnew = np.zeros((Xwin, Ywin))
    
    for i in range(Xwin):
        for j in range(Ywin):
            vizinhos_vivos = int(
                M[(i-1)%Xwin, (j-1)%Ywin] + M[(i-1)%Xwin, j] + M[(i-1)%Xwin, (j+1)%Ywin] +
                M[i, (j-1)%Ywin]                             + M[i, (j+1)%Ywin] +
                M[(i+1)%Xwin, (j-1)%Ywin] + M[(i+1)%Xwin, j] + M[(i+1)%Xwin, (j+1)%Ywin]
            )
            
            if M[i, j] == 1:
                if vizinhos_vivos == 2 or vizinhos_vivos == 3:
                    Mnew[i, j] = 1.0  

            else:
                if vizinhos_vivos == 3:
                    Mnew[i, j] = 1.0  
                    
    return Mnew

pygame.init()       
screen = pygame.display.set_mode((10 * Xwin, 10 * Ywin))
pygame.display.set_caption("Jogo da Vida de Conway")
clock = pygame.time.Clock() # Para controlar a velocidade

inicial(M)

jogando = False

while True:
    screen.fill(BRANCO) 
    desenhaMatriz(M)    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = x // 10, y // 10
            
            M[grid_x, grid_y] = 1.0 if M[grid_x, grid_y] == 0.0 else 0.0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jogando = not jogando
                print(f"Jogo rodando: {jogando}")

    if jogando:
        M = iteracao(M)
        clock.tick(10) 
        
    pygame.display.flip()