import pygame
from random import randint, random

pygame.init()

WIDTH = ___
HEIGHT = ___
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

screen.fill(___)
pygame.display.update()

radius = ___
x = ___
y = ___

pygame.draw.circle(___)  # Position is the center of the circle.


paddle = { "width" : ___,
           "height": ___,
           "color" : ___,
           "x"     : ___,
           "y"     : ___}
paddle["x"] = ___
paddle["y"] = ___
pygame.draw.rect(___)

speed = 5
x_sens = y_sens = 1
pause = False


end = False
while not end:
    screen.fill(___)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        pause = ___

    if key[pygame.K_RETURN]:
        pause = ___

    if key[pygame.K_m]:
        auto = False

    if not pause:

        if key[pygame.K_LEFT]:
            print("Key LEFT pressed")
            ???

        if key[pygame.K_RIGHT]:
            print("Key RIGHT pressed")
            ???

        # change x direction if the ball hits the left or right edge
        ???

        # change y direction if the ball hits the top edge
        ???

         # if the ball hits the paddle top
        ???
            # if the ball is between the x paddle begin and the x paddle end
            ???
                # change y direction
                ???

        # if the ball comes out of the screen from below, end the game
        ???

        # compute the new ball coordinates
        x = x + x_sens * speed
        y = y + y_sens * speed

    # redraw ball and paddle
    pygame.draw.circle(screen, WHITE, (x, y), radius)
    pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    # update screen
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()