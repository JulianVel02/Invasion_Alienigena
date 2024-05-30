import pygame
pygame.init()

# Creacion de ventana
screen = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./images/ufo.png')
pygame.display.set_icon(icon)

# Jugador
player_img = pygame.image.load('./images/jugador.png')
PLAYER_X = 370
PLAYER_Y = 480


def player(x, y):
    """Dibuja la imagen del jugador en las coordenadas dadas"""
    screen.blit(player_img, (x, y))


# Control de FPS
clock = pygame.time.Clock()

# Game Loop
RUNNING = True
while RUNNING:
    screen.fill((0, 0, 0))  # R.G.B

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    # Quiero que el fondo esté activamente en el loop

        # Si keystrock esta presionada, chequear si es derecha o izquierda
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Flecha izquierda esta presionada.")
            if event.key == pygame.K_RIGHT:
                print("Flecha derecha esta presionada.")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_LEFT:
                print("La pulsación de tecla se ha realizado.")

    # Llamo a la funcion despues de imprimir la pantalla
    player(PLAYER_X, PLAYER_Y)
    pygame.display.update()

    # Limitar la tasa de fotogramas
    clock.tick(60)  # 60 FPS

pygame.quit()
