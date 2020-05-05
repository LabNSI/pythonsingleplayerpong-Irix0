import pygame
from random import randint, random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

myfont = pygame.font.SysFont('monospace', 50)

print("pong6")
screen.fill(BLACK)
title = myfont.render("Single Player Pong:", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)

# countdown before start game
# loop from 3 to 0 and write the number in the middle of the screen
???


radius = 10
x = WIDTH//2
y = radius
score = 0

pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.


paddle = { "width" : 200,
           "height": 20,
           "color" : BLUE,
           "x"     : 0,
           "y"     : HEIGHT}
paddle["x"] = WIDTH//2 - paddle["width"]//2
paddle["y"] = HEIGHT - paddle["height"]
pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

speed = 5
x_sens = y_sens = 1
pause = False

end = False
while not end:
    screen.fill(BLACK)
    # Control the game
    # Past your code from pong5.py

    pygame.draw.circle(screen, WHITE, (x, y), radius)
    pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    # Display the score in position (10, 0) (top left on the screen)

    pygame.display.update()
    pygame.time.delay(10)

# Wait a bit to be sure the player knows his score
pygame.time.delay(2000)
pygame.quit()