import random
import matplotlib.pyplot as plt

# Configurações do ambiente da simulação
LARGURA_GRID = 200
ALTURA_GRID = 300

# O raio começa no topo do grid (Nuvem)
raio_x = [LARGURA_GRID // 2]
raio_y = [ALTURA_GRID]

# Conjunto para busca rápida de pontos já ocupados
pontos_ocupados = set([(raio_x[0], raio_y[0])])

# O loop continuará rodando ATÉ que o valor mínimo de Y seja 0 (atingir o solo)
while min(raio_y) > 0:
    # Para espelhar a física real, a ramificação deve ocorrer perto das "pontas" ativas.
    # Escolhemos um ponto aleatório apenas entre os últimos 60 pontos gerados.
    indice_origem = random.randint(max(0, len(raio_x) - 60), len(raio_x) - 1)
    cx, cy = raio_x[indice_origem], raio_y[indice_origem]
    
    # Define as direções de crescimento
    dx = random.choice([-1, 0, 1])
    # 75% de chance de descer (-1) e 25% de andar de lado (0)
    dy = random.choice([-1, -1, -1, 0]) 
    
    # Novas coordenadas geradas
    nx, ny = cx + dx, cy + dy
    
    # Validação do novo ponto (dentro das bordas e não repetido)
    if 0 < nx < LARGURA_GRID and 0 <= ny <= ALTURA_GRID:
        if (nx, ny) not in pontos_ocupados:
            raio_x.append(nx)
            raio_y.append(ny)
            pontos_ocupados.add((nx, ny))

# Criação do Gráfico (Visualização)
plt.figure(figsize=(7, 9), facecolor='black')
ax = plt.axes()
ax.set_facecolor('black')

# Desenha os pontos simulando a descarga elétrica atingindo o chão
plt.scatter(raio_x, raio_y, s=1.2, color='#4DEEEA', alpha=0.7, edgecolors='none')

# Customização estética do gráfico
plt.title("Simulação Fractal: Raio Atingindo o Solo", color='white', fontsize=14, pad=15)
plt.xlim(0, LARGURA_GRID)
plt.ylim(0, ALTURA_GRID)

# Linha verde opcional indicando a superfície do solo
plt.axhline(y=0, color='green', linestyle='-', linewidth=2, alpha=0.5)

# Remove as bordas e eixos para destacar o raio
plt.axis('off')

# Exibe o resultado na tela
plt.show()
