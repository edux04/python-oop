import pygame
import sys

pygame.init()

# Tamaño de la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Personajes que se Mueven")
clock = pygame.time.Clock()
# Clase para el personaje


class Character:
    def __init__(self, x, y, width, height, color, speed, move_keys):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.move_keys = move_keys

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        if keys[self.move_keys[0]]:
            self.x -= self.speed
        if keys[self.move_keys[1]]:
            self.x += self.speed
        if keys[self.move_keys[2]]:
            self.y -= self.speed
        if keys[self.move_keys[3]]:
            self.y += self.speed


# Crear los personajes
player1 = Character(
    50,
    50,
    50,
    50,
    (255, 0, 0),
    1,
    [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN],
)
player2 = Character(
    200, 200, 50, 50, (0, 0, 255), 2, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]
)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player1.move(keys)
    player2.move(keys)

    win.fill((0, 0, 0))  # Limpia la pantalla

    player1.draw(win)
    player2.draw(win)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
