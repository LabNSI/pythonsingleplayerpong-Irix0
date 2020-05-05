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
pygame.display.update()

radius = 25
x = WIDTH//2
y = HEIGHT//2
pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.

speed = 1
x_sens = y_sens = 1
auto = True


end = False
while not end:
    screen.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_o]:
        print("Key O pressed")
        print("Mode Auto")
        auto = ___

    if key[pygame.K_m]:
        print("Key M pressed")
        print("Mode Manuel")
        auto = ___

    if not auto:
        # Manual mode :
        #  - use A, Z, Q, S to move circle on the corners
        #  - use UP, DOWN, LEFT, RIGHT to move circle by <speed> pixel

        if key[pygame.K_a]:
            print("Key A pressed")
            x = radius
            y = radius

        if key[pygame.K_z]:
            print("Key Z pressed")
            x = WIDTH - radius
            y = radius

        if key[pygame.K_q]:
            print("Key Q pressed")
            x = radius
            y = HEIGHT - radius

        if key[pygame.K_s]:
            print("Key S pressed")
            x = WIDTH - radius
            y = HEIGHT - radius

        if key[pygame.K_UP]:
            print("Key UP pressed")
            ???

        if key[pygame.K_DOWN]:
            print("Key DOWN pressed")
            ???

        if key[pygame.K_LEFT]:
            print("Key LEFT pressed")
            ???

        if key[pygame.K_RIGHT]:
            print("Key RIGHT pressed")
            ???

    else:
        # if the circle touches the right and left edges
        # reverse direction on x-axis
        if ____:
            x_sens = ____

        # if the circle touches the lower and upper edges
        # reverse direction on y-axis
        if ___:
            y_sens = ___

        # compute new coordonates
        x = x + ___
        y = y + ___


    pygame.draw.circle(screen, WHITE, (x, y), radius)

    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()