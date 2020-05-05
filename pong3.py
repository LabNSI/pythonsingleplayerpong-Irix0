import pygame

pygame.init()

WIDTH = 300
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

screen.fill(RED)
pygame.display.flip()

radius = 25
x = WIDTH//2
y = HEIGHT//2
pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.


end = False
while not end:
    # fill screen with color only
    screen.____
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.___

    if ___:
        # up left corner

    if ___:
        # up right corner

    if ___:
        # down left corner

    if ___:
        # down left corner

    # redraw circle at new position
    ___
    # update the display
    pygame.display.update()

pygame.quit()