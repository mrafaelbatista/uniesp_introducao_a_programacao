import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições da tela
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamanho da cobrinha e dos alimentos
BLOCK_SIZE = 20

# Velocidade da cobrinha
SPEED = 10

# Função para desenhar a cobrinha
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(SCREEN, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Função para gerar alimentos em posições aleatórias
def spawn_food():
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return food_x, food_y

# Função principal do jogo
def main():
    # Inicialização da cobrinha
    snake = [[WIDTH / 2, HEIGHT / 2]]
    snake_direction = "RIGHT"

    # Inicialização do movimento da cobrinha
    move_x = 0
    move_y = 0

    # Inicialização do alimento
    food_x, food_y = spawn_food()

    # Loop principal do jogo
    running = True
    while running:
        # Verificação de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                    move_x = 0
                    move_y = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                    move_x = 0
                    move_y = BLOCK_SIZE
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                    move_x = -BLOCK_SIZE
                    move_y = 0
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"
                    move_x = BLOCK_SIZE
                    move_y = 0

        # Movimentação da cobrinha
        snake[0][0] += move_x
        snake[0][1] += move_y

        # Verificação de colisões com as bordas
        if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
            running = False

        # Verificação de colisões com o próprio corpo
        if snake[0] in snake[1:]:
            running = False

        # Verificação de colisões com o alimento
        if snake[0][0] == food_x and snake[0][1] == food_y:
            snake.append([food_x, food_y])
            food_x, food_y = spawn_food()

        # Limpeza da tela
        SCREEN.fill(WHITE)

        # Desenho da cobrinha e do alimento
        draw_snake(snake)
        pygame.draw.rect(SCREEN, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Atualização da tela
        pygame.display.flip()

        # Controle de velocidade
        pygame.time.Clock().tick(SPEED)

    # Finalização do Pygame
    pygame.quit()

# Execução do jogo
if __name__ == "__main__":
    main()
